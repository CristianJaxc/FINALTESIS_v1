from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect
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
from app.usuario.models import Perfil
from app.denuncias.models import Denuncias
from app.home.models import Contactos
from app.adopciones.models import Perros
from app.servicios.models import  Category,Product
from app.cart import cart
from app.donaciones.models import *
from app.usuario.models import *
from app.servicios.models import Product,ImagenProducto,Category

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# ---------- Para Formularios -------------
from app.denuncias.forms import DenunciasForm, DenunciasForm2
from app.home.forms import ContactosForm
from django.utils.decorators import method_decorator

# ---------- Para Traducciones -------------

from django.utils import translation
# Create your views here.


def index(request):
    language = request.session.get(translation.LANGUAGE_SESSION_KEY)  
    if language =='en':
  
        data={  
            'donaciones':Productos.objects.all(),
            'voluntariado':Perfil.objects.all(),
            'denuncias':Denuncias.objects.all(),
            'mascotas':Perros.objects.all(),
            'Ventas':Product.objects.all(),

                }

        
        return render(request,"home/index2.html",data)
    else: 
            data={  
            'donaciones':Productos.objects.all(),
            'voluntariado':Perfil.objects.all(),
             'denuncias':Denuncias.objects.all(),
            'mascotas':Perros.objects.all(),
            'Ventas':Product.objects.all(),

                }

        
            return render(request,"home/index.html",data) 


@login_required(login_url='/accounts/login')
def prueba(request):


    usuarios=request.user.id
    voluntario3=request.user.perfil.role
    #datos=User.objects.get(id=usuario)
    #if datos.is_superuser:
    if voluntario3 == 'usuario':
        #return render(request, 'voluntarios/pagina_voluntario.html')
        return render(request, 'cliente/pagina_cliente.html')
    else :
        return render(request, 'administracion/pagina.html')

@login_required
def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('perfil')
    return render(request, 'registration/sign_up.html', {'form': form})

#?-------------------------- Contactos --------------------------------------

class ContactoCreate(SuccessMessageMixin, generic.CreateView):
    # modelos de datos
    model = Contactos
    # Formularios de datos
    form_class = ContactosForm
    # success forms
    template_name = 'contactos/contactos_pagina.html'
    success_url = reverse_lazy('home')
    @method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs): #pinto el formulario en el html
        context = super(ContactoCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
        
            new = form.save(commit=False)
            form.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Contactos_Listado(SuccessMessageMixin, ListView):
    model = Contactos
    template_name = 'contactos/contactos_listado.html'
    def get_queryset(self):
            return Contactos.objects.all().order_by('id')

class ContactoDetail(SuccessMessageMixin, TemplateView):
    template_name = 'contactos/contactos_detalle.html'
    def get_context_data(self, **kwargs):
        context = super(ContactoDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        contactos = Contactos.objects.get(id = pk)
        #print(usuario.username)
        return {'contactos':contactos}


class Eliminar_Contacto(DeleteView):
    model =Contactos
    template_name = 'contactos/contactos_eliminar.html'
    success_url=reverse_lazy('contacto_listado')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_Contacto, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('contacto_listado')
        return context



def quienes_somos(request):
        return render(request,"contactos/contacto_directo.html")


class ContactoVoluntario(SuccessMessageMixin, generic.CreateView):
    # modelos de datos
    model = Contactos
    # Formularios de datos
    form_class = ContactosForm
    # success forms
    template_name = 'blogs/solicitud_voluntario.html'
    success_url = reverse_lazy('pagina_blogs')

    def get_context_data(self, **kwargs):  # pinto el formulario en el html
        context = super(ContactoVoluntario, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():

            new = form.save(commit=False)
            form.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
