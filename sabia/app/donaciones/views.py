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

from app.usuario.models import Perfil
from app.denuncias.models import Denuncias
from app.donaciones.models import Solicitudes, Productos
from app.donaciones.forms import Solicitudes_donacion_Form, Solicitudes_donacion_Form2, ProductosForm
# ---------- Para Formularios -------------
from app.denuncias.forms import DenunciasForm, DenunciasForm2
from django.utils.decorators import method_decorator

# Create your views here.

def Pagina_donaciones(request):
    productos = Productos.objects.all().order_by('id')
    return render(request, 'donaciones/pagina_donaciones.html',{'productos':productos})

class Listado_donaciones(SuccessMessageMixin, ListView):
    model = Productos
    template_name = 'donaciones/listado_donaciones.html'
    def get_queryset(self):
            return Productos.objects.all().order_by('id')

class Registrar_Producto(SuccessMessageMixin, generic.CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = 'donaciones/registrar_donaciones.html'
    success_url = reverse_lazy('listado_donaciones')

    def get_context_data(self, **kwargs): #pinto el formulario en el html
        context = super(Registrar_Producto, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            
            new = form.save(commit=False)
            form.save()
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Editar_Producto(SuccessMessageMixin, UpdateView):
    model = Productos
    form_class = ProductosForm
    template_name = 'donaciones/editar_donaciones.html'

    def get_context_data(self,**kwargs):
        context = super(Editar_Producto, self).get_context_data(**kwargs)
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
        form = self.form_class(request.POST, request.FILES, instance = producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('listado_donaciones'))
        else:
            return HttpResponseRedirect(reverse_lazy('listado_donaciones'))

#!---------------------- Solicitudes de donaciones ------------------------------

class Listado_Solicitudes_donaciones(SuccessMessageMixin, ListView):
    model = Solicitudes
    template_name = 'donaciones/solicitudes/listado_solicitudes_donaciones.html'
    def get_queryset(self):
            return Solicitudes.objects.all().order_by('id')

class Solicitud_donacion(SuccessMessageMixin, generic.CreateView):
    model = Solicitudes
    form_class = Solicitudes_donacion_Form
    template_name = 'donaciones/solicitudes/generar_solicitud_donacion.html'
    success_url = reverse_lazy('pagina_donaciones')

    def get_context_data(self, **kwargs):
        context = super(Solicitud_donacion, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        print(pk)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        pk = self.kwargs.get('pk', 0)
        print(pk)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            
            new = form.save(commit=False)
            new.productos_id = pk
            form.save()
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Solicitud_detalle_donacion(SuccessMessageMixin, TemplateView):
    template_name = 'donaciones/solicitudes/detalle_solicitud_donacion.html'
    def get_context_data(self, **kwargs):
        context = super(Solicitud_detalle_donacion, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = Solicitudes.objects.get(id = pk)
        producto = Productos.objects.get(id = solicitud.productos_id)
        return {'solicitud':solicitud, 'producto':producto}

class editar_solicitud_donacion(SuccessMessageMixin, UpdateView):
    model = Solicitudes
    form_class = Solicitudes_donacion_Form2
    template_name = 'donaciones/solicitudes/editar_solicitud_donaciones.html'

    def get_context_data(self,**kwargs):
        context = super(editar_solicitud_donacion, self).get_context_data(**kwargs)
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
            return HttpResponseRedirect(reverse_lazy('detalle_solicitud_donacion', kwargs=kwargs))
        else:
            return HttpResponseRedirect(reverse_lazy('detalle_solicitud_donacion', kwargs=kwargs))

class Eliminar_donacion(DeleteView):
    model = Productos
    template_name = 'donaciones/eliminar_donaciones.html'
    success_url=reverse_lazy('listado_donaciones')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_donacion, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('listado_donaciones')
        return context 


class Eliminar_solicitud(DeleteView):
    model = Solicitudes
    template_name = 'donaciones/solicitudes/eliminar_solicitud.html'
    success_url=reverse_lazy('listado_solicitudes_donaciones')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_solicitud, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('listado_solicitudes_donaciones')
        return context

# ------------------ APADRINAMIENTO :::  -------------------
def Pagina_apdrinamiento(request):
    productos = Productos.objects.all().order_by('id')
    return render(request, 'donaciones/pagina_apadrinamiento.html',{'productos':productos})

