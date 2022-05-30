from pipes import Template
from pyexpat import model
from urllib import request
from venv import create
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView
# ----------- Para Mesnsajes -------------
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# ---------- Para modelos -------------
from django.contrib.auth.models import User
from app.blogs.models import Blogs
from app import usuario
from app.usuario.models import Perfil




# ---------- Para Formularios -------------
from app.usuario.forms import PerfilForm, UpdateUserForm
from django.utils.decorators import method_decorator
from app.blogs.forms import BlogsForm, BlogsForm2




# Create your views here.


@method_decorator(login_required, name='dispatch')
class volunView(SuccessMessageMixin, generic.CreateView):

    def userlog(request):
      
      
        a=request.user.id
        id_usuario=User.objects.get(id=a)
        print(id_usuario.id)
        a=UserLogeado_u=id_usuario.username
        b=UserLogeado_p=id_usuario.password
        return a,b

    # modelos de datos
    model = Perfil

    # Formularios de datos
    form_class = PerfilForm
    # success forms
    template_name = 'voluntarios/perfil_volun.html'
    success_url = reverse_lazy('pagina')

    def get_context_data(self, **kwargs): #pinto el formulario en el html
        context = super(volunView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_usu = self.request.user.id #usuario logeado
        form = self.form_class(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.User_id = id_usu
            form.save()
            print(new.User_id)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Detail_Usu(SuccessMessageMixin, TemplateView):
    model = Blogs
    form_class = BlogsForm

  

    template_name = 'voluntarios/detalleperfil_volunt.html'
    def get_context_data(self, **kwargs):
       
    
        context = super(Detail_Usu, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        usuario = User.objects.get(id=pk)
        perfil = Perfil.objects.get(User_id = pk)
        # comentario , create=Blogs.objects.get_or_create(User_id=pk)
      
        # try:
        #     comentario = Blogs.objects.get(id=pk)
    

        #     # comentario = Blogs.objects.get(User_id = pk)
        #     return {'usuario': usuario, 'perfil':perfil,'comentario':comentario}
        # except comentario.DoesNotExist:
        #     comentario ='no existe comentario '
        #     return {'usuario': usuario, 'perfil':perfil,'comentario':comentario}
      
        return {'usuario': usuario, 'perfil':perfil}
    
       
        
    
        #print(usuario.username)
   


class Mi_Usuario_Update(SuccessMessageMixin, UpdateView):
    model = User
    second_model = Perfil
    template_name = 'voluntarios/editar_perfil.html'
    form_class = UpdateUserForm
    second_form_class = PerfilForm
    
    def get_context_data(self,**kwargs):
        context = super(Mi_Usuario_Update, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        usuario_editar = self.model.objects.get(id = pk_editar)
        usuario_editar_perfil= self.second_model.objects.get(User_id = usuario_editar.id)
        #print(usuario_editar.id,'aca el otro',usuario_editar_perfil.id)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = usuario_editar)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = usuario_editar_perfil)
        context['id'] = pk_editar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_user = kwargs['pk']
        user2 = self.model.objects.get(id = id_user)
        usuario2 = self.second_model.objects.get(User_id = user2.id)
        form = self.form_class(request.POST, instance = user2)
        form2 = self.second_form_class(request.POST, instance = usuario2)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(reverse_lazy('detalle_perfil', kwargs=kwargs))
        else:
            return HttpResponseRedirect(reverse_lazy('detalle_perfil', kwargs=kwargs))


class Listado_usuarios(SuccessMessageMixin, ListView):
    model = User
    template_name = 'administracion/usuarios/listado_usuarios.html'
    
    def get_queryset(self):
            return User.objects.all().order_by('id')

class quienes_somos(SuccessMessageMixin, ListView):
    model = User
    template_name = 'administracion/usuarios/quienesSomos.html'
    def get_queryset(self):
            return User.objects.all().order_by('id')


class Detalle_usuario(SuccessMessageMixin, TemplateView):
    template_name = 'administracion/usuarios/detalle_usuario.html'
    def get_context_data(self, **kwargs):
        context = super(Detalle_usuario, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        usuario = User.objects.get(id = pk)
        perfil = Perfil.objects.get(User_id = usuario.id)
        return {'usuario':usuario, 'perfil':perfil}




class Eliminar_usuario(DeleteView):
    model = User
    template_name = 'administracion/usuarios/eliminar_usuario.html'
    success_url=reverse_lazy('listado_usuarios')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_usuario, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('listado_usuarios')
        return context 

