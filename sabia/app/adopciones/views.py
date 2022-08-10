from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView
# ----------- Para Mesnsajes -------------
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# ---------- Para modelos -------------
from django.contrib.auth.models import User
from app.adopciones.forms import PerroForm, SolicitudesForm, SolicitudesForm2
from app.adopciones.models import Perros, Solicitudes,Categorias_Perros

from app.usuario.models import Perfil
from app.denuncias.models import Denuncias
# ---------- Para Formularios -------------
from app.denuncias.forms import DenunciasForm, DenunciasForm2
from django.utils.decorators import method_decorator

#-----------paginacion 
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def Pagina_adopciones_terminos(request):

     return render(request, 'adopciones/perros/terminos_adopcion.html')

def Pagina_adopciones(request):

     perros = Perros.objects.filter(estado = True).order_by('id')
     queryset=request.GET.get("buscar")
     #page = request.GET.get("page") or 1
     page_number = request.GET.get('page')

     if queryset:
      perros=Perros.objects.filter(
          Q(nombre__icontains=queryset)
     ).distinct()
     try :
         paginator = Paginator(perros,6)
         page_obj = paginator.get_page(page_number)
         perros = paginator.page(page_number)
        #paginator = Paginator(perros,6)
        #perros = paginator.page(page)
     except Exception as e:
         print(e)
    #  paginate_by=1
    #  queryset= Perros.objects.filter(estado = True).order_by('id')
    #  paginate_by=1
     return render(request, 'adopciones/pagina_adopciones.html',{'perros':perros,'page_obj':page_obj})





def get_queryset(self):
      
      return Perros.objects.filter(estado = True).order_by('id')


#Clasificacion mascotas , sexo , tamaño .:
def perro_list(request, category_slug=None):
    category = None
    categories = Categorias_Perros.objects.all()
    perros = Perros.objects.filter(estado=True).order_by('id')
    queryset = request.GET.get("buscar")
    # page = request.GET.get("page") or 1
    page_number = request.GET.get('page')

    if queryset:
        perros = Perros.objects.filter(
            Q(nombre__icontains=queryset)
        ).distinct()
    try:
        paginator = Paginator(perros, 6)
        page_obj = paginator.get_page(page_number)
        perros = paginator.page(page_number)
    # paginator = Paginator(perros,6)
    # perros = paginator.page(page)
    except Exception as e:
        print(e)



    if category_slug:
        category = get_object_or_404(Categorias_Perros, slug=category_slug)
        perros = perros.filter(category=category)

    return render(request, 'adopciones/pagina_adopciones2.html',
                  {'category': category, 'categories': categories,
                   'perros': perros,'page_obj':page_obj})

# class pagina_adopciones(ListView):
#      template_name='adopciones/pagina_adopciones.html'
#      model = Perros
  
      
     

#      def get_queryset(self):
      
#       return Perros.objects.filter(estado = True).order_by('id')

#      paginate_by=1
#             #  return Perros.objects.filter(estado = True).order_by('id')
#     #  queryset=request.GET.get("buscar")
 
#     #  if queryset:
#     #      perros=Perros.objects.filter(
#     #          Q(nombre=queryset)
#     #      ).distinct()
#      def get_context_data(self, **kwargs):
#          context=super().get_context_data(**kwargs)
#         #  context['perros'] = self.get_queryset()
   
#          context['messsage']='Listado de Perros'
#          return context

     
        
    

class adopciones_Listado(SuccessMessageMixin, ListView):
    model = Solicitudes
    template_name = 'adopciones/adopciones_listado.html'
    def get_queryset(self):
            return Solicitudes.objects.all().order_by('id')

class SolicitudCreate(SuccessMessageMixin, generic.CreateView):
    model = Solicitudes
    form_class = SolicitudesForm
    template_name = 'adopciones/solicitudes/registrar_solicitud.html'
    success_url = reverse_lazy('pagina_adopciones2')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        print(pk)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        pk = self.kwargs.get('pk', 0)
        print(pk)
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            
            new = form.save(commit=False)
            new.perros_id = pk
            form.save()
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SolicitudDetail(SuccessMessageMixin, TemplateView):
    template_name = 'adopciones/solicitudes/detalle_solicitud.html'
    def get_context_data(self, **kwargs):
        context = super(SolicitudDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = Solicitudes.objects.get(id = pk)
        perro = Perros.objects.get(id = solicitud.perros_id)
        return {'solicitud':solicitud, 'perro':perro}

class SolicitudUpdate(SuccessMessageMixin, UpdateView):
    model = Solicitudes
    form_class = SolicitudesForm2
    template_name = 'adopciones/solicitudes/editar_solicitud.html'

    def get_context_data(self,**kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
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
        perro = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = perro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('detalle_solicitud', kwargs=kwargs))
        else:
            return HttpResponseRedirect(reverse_lazy('detalle_solicitud', kwargs=kwargs))


#!------------------------- administrar perros --------------------------
class PerroCreate(SuccessMessageMixin, generic.CreateView):
    # modelos de datos
    model = Perros
    # Formularios de datos
    form_class = PerroForm
    # success forms
    template_name = 'adopciones/perros/registrar_perro.html'
    success_url = reverse_lazy('listado_perro')

    def get_context_data(self, **kwargs): #pinto el formulario en el html
        context = super(PerroCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            
            new = form.save(commit=False)
            form.save()
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Perro_Listado(SuccessMessageMixin, ListView):
    model = Perros
    template_name = 'adopciones/perros/listado_perro.html'
    def get_queryset(self):
            return Perros.objects.all().order_by('id')

class PerroDetail(SuccessMessageMixin, TemplateView):
    model = Solicitudes
    form_class = SolicitudesForm
    template_name = 'adopciones/perros/detalle_perro.html'
    success_url = reverse_lazy('listado_perro')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            action = request.POST['action']
            if action == 'add':

                con = Solicitudes()
                con.nombre= request.POST['nombre']
                con.apellido = request.POST['apellido']
                con.cedula = request.POST['cedula']
                con.telefono = request.POST['telefono']
                con.direccion = request.POST['direccion']
                con.descripcion = request.POST['descripcion']
                con.perros = request.POST['perros']
                con.save()


            else:
                data['error'] = 'ha ocurrido un error'
            # data = Product.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = data
            # print(Product.objects.get(pk=request.POST['id']))
            # print(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    def get_context_data(self, **kwargs):
        context = super(PerroDetail, self).get_context_data(**kwargs)
        context['list_url'] = reverse_lazy('pagina_blogs')
        context['form'] = SolicitudesForm()
        context['action'] = 'add'
        pk = self.kwargs.get('pk', 0)
        context['perro']  = Perros.objects.get(id = pk)
        
        return context

class PerroUpdate(SuccessMessageMixin, UpdateView):
    model = Perros
    form_class = PerroForm
    template_name = 'adopciones/perros/editar_perro.html'

    def get_context_data(self,**kwargs):
        context = super(PerroUpdate, self).get_context_data(**kwargs)
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
        perro = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = perro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('detalle_perro', kwargs=kwargs))
        else:
            return HttpResponseRedirect(reverse_lazy('detalle_perro', kwargs=kwargs))


# ELIMINACION DE SOLICITUD 


class Eliminar_Solicitud(DeleteView):
    model =Solicitudes
    template_name = 'adopciones/eliminar_solicitud.html'
    success_url=reverse_lazy('adopciones_listado')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_Solicitud, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('adopciones_listado')
        return context 

class Eliminar_Perro(DeleteView):
    model =Perros
    template_name = 'adopciones/perros/eliminar_perro.html'
    success_url=reverse_lazy('listado_perro')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_Perro, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('listado_perro')
        return context 
