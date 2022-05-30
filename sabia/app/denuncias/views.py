from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView
# ----------- Para Mesnsajes -------------
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# ---------- Para modelos -------------
from django.contrib.auth.models import User
from app.usuario.models import Perfil
from app.denuncias.models import Denuncias
# ---------- Para Formularios -------------
from app.denuncias.forms import DenunciasForm, DenunciasForm2
from django.utils.decorators import method_decorator

# Create your views here.

def Pagina_denuncias(request):
    denuncias = Denuncias.objects.filter(estado = True).order_by('id')
    return render(request, 'denuncias/pagina_denuncias.html',{'denuncias':denuncias})

class Denuncias_Listado(SuccessMessageMixin, ListView):
    model = Denuncias
    template_name = 'denuncias/denuncias_list.html'
    def get_queryset(self):
            return Denuncias.objects.all().order_by('id')

class DenuciaCreate(SuccessMessageMixin, generic.CreateView):
    # modelos de datos
    model = Denuncias
    # Formularios de datos
    form_class = DenunciasForm
    # success forms
    template_name = 'denuncias/registro_denuncias.html'
    success_url = reverse_lazy('denuncias_listado')

    def get_context_data(self, **kwargs): #pinto el formulario en el html
        context = super(DenuciaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            
            new = form.save(commit=False)
            form.save()
            print(new.descripcion, ' -> ', new.id)
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class DenunciaDetail(SuccessMessageMixin, TemplateView):
    template_name = 'denuncias/denuncias_detalle.html'
    def get_context_data(self, **kwargs):
        context = super(DenunciaDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        denuncias = Denuncias.objects.get(id = pk)
        #print(usuario.username)
        return {'denuncias':denuncias}

class DenunciaUpdate(SuccessMessageMixin, UpdateView):
    model = Denuncias
    form_class = DenunciasForm2
    template_name = 'denuncias/denuncias_editar.html'

    def get_context_data(self,**kwargs):
        context = super(DenunciaUpdate, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        denuncia_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = denuncia_editar)
        context['id'] = pk_editar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        denuncia = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = denuncia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('denuncias_detalle', kwargs=kwargs))
        else:
            return HttpResponseRedirect(reverse_lazy('denuncias_detalle', kwargs=kwargs))

class Eliminar_denuncia(DeleteView):
    model = Denuncias
    template_name = 'denuncias/denuncias_eliminar.html'
    success_url=reverse_lazy('denuncias_listado')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_denuncia, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('denuncias_listado')
        return context 
