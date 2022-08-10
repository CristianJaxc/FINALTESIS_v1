from django.http import JsonResponse
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
from app import blogs
# ---------- Para modelos -------------
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from app.blogs.models import Blogs, Noticia ,NotiInfo
from app.blogs.forms import BlogsForm, BlogsForm2,NoticiaBlogForm,NoticiaForm
from app.usuario.models import Perfil
from app.denuncias.models import Denuncias
from app.donaciones.models import Solicitudes, Productos
from app.donaciones.forms import Solicitudes_donacion_Form, Solicitudes_donacion_Form2, ProductosForm
from app.home.forms import ContactosForm
from app.home.models import Contactos
# ---------- Para Formularios -------------
from app.denuncias.forms import DenunciasForm, DenunciasForm2
from django.utils.decorators import method_decorator

# Create your views here.

def Pagina_Noticia(request):
    Noti = Noticia.objects.filter(estado=True).order_by('fecha_creacion')
    contact_list =Noticia.objects.all()
    paginator = Paginator(contact_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    NotiInforma =  NotiInfo.objects.all()
    return render(request, 'administracion/usuarios/quienesSomos.html',{'Noti':Noti,'page_obj': page_obj,'NotiInforma':NotiInforma})


#def Pagina_blogs(request):
   # blogs = Blogs.objects.filter(estado=True)
   # return render(request, 'blogs/pagina_blogs.html',{'blogs':blogs})


class Pagina_blogs(SuccessMessageMixin, generic.CreateView):
    model = Contactos
    form_class = ContactosForm
    template_name = 'blogs/pagina_blogs.html'
    success_url = reverse_lazy('pagina_blogs')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            action = request.POST['action']
            if action == 'add':
               con=Contactos()
               con.nombres = request.POST['nombres']
               con.apellidos= request.POST['apellidos']
               con.email = request.POST['email']
               con.telefono = request.POST['telefono']
               con.descripcion = request.POST['descripcion']
               con.save()

            else:
                data['error'] = 'ha ocurrido un error'
            # data = Product.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = data
            # print(Product.objects.get(pk=request.POST['id']))
            # print(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super(Pagina_blogs, self).get_context_data(**kwargs)
        context['title'] = 'Reporte de ventas'
        context['entity'] = "Despliegue de reportes de ventas"
        context['list_url'] = reverse_lazy('pagina_blogs')
        context['form'] = ContactosForm()
        context['action'] = 'add'
        context['blogs'] = Blogs.objects.filter(estado=True)
        return context



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


# ---------- Para Noticia  -------------

class Listado_Noticias(SuccessMessageMixin, ListView):
    model = Noticia
    template_name = 'administracion/Noticia/listado_noticia.html'

    def get_queryset(self):
        return Noticia.objects.all().order_by('id')
# ---------- Registrar Noticia -------------


class Registrar_Noticia(SuccessMessageMixin, generic.CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'administracion/Noticia/registrar_noticia.html'
    success_url = reverse_lazy('pagina_noticia')

    def get_context_data(self, **kwargs):  # pinto el formulario en el html
        context = super(Registrar_Noticia, self).get_context_data(**kwargs)
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
# ---------- Actualziar Noticia  -------------


class NotiUpdate(SuccessMessageMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'administracion/Noticia/actualizar_noticia.html'
    success_url = reverse_lazy('listado_noticia')
    def get_context_data(self,**kwargs):
        context = super(NotiUpdate, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        noticia_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = noticia_editar)
        context['id'] = pk_editar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        noticia = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = noticia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


# ---------- Eliminar  Noticia  -------------


class Eliminar_Noticia(DeleteView):
    model =Noticia
    template_name = 'administracion/Noticia/eliminar_noticia.html'
    success_url=reverse_lazy('listado_noticia')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_Noticia, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('listado_noticia')
        return context

# ---------- PARA EL ANTES Y DESPUES - VIDEOS DE LA SECCION -------------

class Listado_Noticias_blogs(SuccessMessageMixin, ListView):
    model = NotiInfo
    template_name = 'administracion/Noticia/listado_notiblog.html'

    def get_queryset(self):
        return NotiInfo.objects.all().order_by('id')


# ---------- Registrar Contenido -------------

class Registrar_Noticia_blogs(SuccessMessageMixin, generic.CreateView):
    model = NotiInfo
    form_class = NoticiaBlogForm
    template_name = 'administracion/Noticia/registrar_noticia_blog.html'
    success_url = reverse_lazy('listado_noticia_blogs')

    def get_context_data(self, **kwargs):  # pinto el formulario en el html
        context = super(Registrar_Noticia_blogs, self).get_context_data(**kwargs)
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


# ---------- Actualziar Contenido -------------


class Noti_blog_Update(SuccessMessageMixin, UpdateView):
    model = NotiInfo
    form_class = NoticiaBlogForm
    template_name = 'administracion/Noticia/actualizar_noticia_blog.html'
    success_url = reverse_lazy('listado_noticia_blogs')
    def get_context_data(self,**kwargs):
        context = super(Noti_blog_Update, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        noticia_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = noticia_editar)
        context['id'] = pk_editar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        noticia = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = noticia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())



# ---------- Eliminar  Contenido -------------

class Eliminar_Noticia_blog(DeleteView):
    model = NotiInfo
    template_name = 'administracion/Noticia/eliminar_noticia_blog.html'
    success_url=reverse_lazy('listado_noticia_blogs')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_Noticia_blog, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('listado_noticia_blogs')
        return context
