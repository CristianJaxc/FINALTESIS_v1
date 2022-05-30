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
from app import blogs
# ---------- Para modelos -------------
from django.contrib.auth.models import User
from app.blogs.models import Blogs
from app.blogs.forms import BlogsForm, BlogsForm2
from app.usuario.models import Perfil
from app.denuncias.models import Denuncias
from app.donaciones.models import Solicitudes, Productos
from app.donaciones.forms import Solicitudes_donacion_Form, Solicitudes_donacion_Form2, ProductosForm
# ---------- Para Formularios -------------
from app.denuncias.forms import DenunciasForm, DenunciasForm2
from django.utils.decorators import method_decorator

# Create your views here.

def Pagina_blogs(request):
    blogs = Blogs.objects.filter(estado=True)
    return render(request, 'blogs/pagina_blogs.html',{'blogs':blogs})

class Listado_blogs(SuccessMessageMixin, ListView):
    model = Blogs
    template_name = 'blogs/listado_blogs.html'


    
    def get_queryset(self):
            return Blogs.objects.all().order_by('id')

class Registrar_Blogs(SuccessMessageMixin, generic.CreateView):
    model = Blogs
    form_class = BlogsForm
    template_name = 'blogs/registrar_blogs.html'
    success_url = reverse_lazy('pagina_blogs')

    def get_context_data(self, **kwargs): #pinto el formulario en el html
        context = super(Registrar_Blogs, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_usu = self.request.user.id
        form = self.form_class(request.POST)
        if form.is_valid():
            
            new = form.save(commit=False)
            new.User_id = id_usu
            form.save()
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Editar_blogs(SuccessMessageMixin, UpdateView):
    model = Blogs
    form_class = BlogsForm2
    template_name = 'blogs/editar_blogs.html'

    def get_context_data(self,**kwargs):
        context = super(Editar_blogs, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        perro_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = perro_editar)
        context['id'] = pk_editar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        producto = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, instance = producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('listado_blogs'))
        else:
            return HttpResponseRedirect(reverse_lazy('listado_blogs'))

class DetalleDeleteView(DeleteView):
    model = Blogs
    form_class = BlogsForm2
    template_name = 'blogs/delete.html'
    success_url=reverse_lazy('listado_blogs')


    def get_context_data(self,**kwargs):
        context = super(DetalleDeleteView, self).get_context_data(**kwargs)
        context['action']='edit'
        context['list_url']=reverse_lazy('listado_blogs')
        return context 


class Detalle_blogs(SuccessMessageMixin, TemplateView):
    template_name = 'blogs/detalle_blogs.html'
    def get_context_data(self, **kwargs):
        context = super(Detalle_blogs, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        blogs = Blogs.objects.get(id = pk)
        usuario = User.objects.get(id = blogs.User_id)
        return {'blogs':blogs, 'usuario':usuario}