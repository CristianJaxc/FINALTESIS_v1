from django.shortcuts import render
from .models import Product,Category,ImagenProducto
from app.cliente.models import Client
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect
#MENSAJERIA ::
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView
from django.forms.models import inlineformset_factory
from django.contrib import messages
from app.cart.forms import CartAddProductForm
from .forms import *
from app.orders.models import OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.

def esterilizacion(request):

        return render(request, 'servicios/esterilizacion.html')


def pagina_productos(request):

        product = Product.objects.filter(available=True)

        return render(request,"servicios/productos.html",{
                "product": product
        })




def product_list(request, category_slug=None):
    model = Client
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'servicios/listado_productos.html',
                  {'category': category, 'categories': categories,
                   'products': products})



#def product_detail(request, id, slug):
  #  product = get_object_or_404(Product, id=id, slug=slug, available=True)
   # return render(request, 'servicios/detalle_productos.html', {'product': product})



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    product_similar = Product.objects.all().order_by('category')
    cart_product_form = CartAddProductForm()

    return render(request, 'servicios/detalle_productos.html',
                  {'product': product, 'cart_product_form': cart_product_form,'product_similar':product_similar})



class Listado_Productos(SuccessMessageMixin, ListView):
    model = Product
    template_name = 'servicios/cart/listar_producto.html'
    def get_queryset(self):
            return Product.objects.all().order_by('id')
#---------------------------------------------SECCION ADMINISTRACION ----------------------------------
#REGISTRAR PRODUCTOS ::

class Registrar_Producto(generic.CreateView):
    model = Product
    form_class = ProductoForm
    template_name = 'servicios/cart/agregar_producto.html'
    success_url = reverse_lazy('listar_productos')

    def get_context_data(self, **kwargs):  # pinto el formulario en el html
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

#PRUEBA DE REGISTRO DE IMAGENES :

#class Registrar_Imagenes(SuccessMessageMixin, generic.CreateView):

        #   def Imagenes(request):
        #a = request.ImageProducto.id
        #id_usuario = Product.objects.get(id=a)
        #return a,id_usuario
    # modelos de datos
    #model = ImagenProducto
    #secondo_model = Product
    # Formularios de datos
    #form_class = ImagenesForm
    #seconf_form = ProductoForm
    # success forms
    #template_name = 'servicios/cart/añadir_imagenes.html'
    # success_url = reverse_lazy('listar_productos')

    #def get_context_data(self, **kwargs):  # pinto el formulario en el html
        #context = super(Registrar_Imagenes, self).get_context_data(**kwargs)
            # if 'form' not in context:
        # context['form'] = self.form_class(self.request.GET)

    #  return context

    #def post(self, request, *args, **kwargs):
        #self.object = self.get_object
        #id_usu = self.request.user.id  # usuario logeado
        # form = self.form_class(request.POST,request.FILES)
            # if form.is_valid():
            # new = form.save(commit=False)
            #new.User_id = id_usu
            # form.save()
        # return HttpResponseRedirect(self.get_success_url())
            # else:
# return self.render_to_response(self.get_context_data(form=form))




class Editar_Producto(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductoForm
    second_model = ImagenProducto
    form_class2 = ImagenesForm
    template_name = 'servicios/cart/editar_producto.html'

    def get_context_data(self,**kwargs):
        context = super(Editar_Producto, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        producto_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = producto_editar)
        context['id'] = pk_editar
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        producto = self.model.objects.get(id = id_editar)
        #imagenes = self.second_model.objects.get(Image_id=producto.id)
        form = self.form_class(request.POST, request.FILES, instance = producto)
        #form2 = self.form_class2(request.POST, instance = imagenes)
        if form.is_valid() :
            form.save()

            return HttpResponseRedirect(reverse_lazy('listar_productos'))
        else:
            return HttpResponseRedirect(reverse_lazy('listar_productos'))

class Eliminar_Producto(DeleteView):
    model = Product
    template_name =  'servicios/cart/eliminar_producto.html'
    success_url=reverse_lazy('listar_productos')
    def get_context_data(self,**kwargs):

        context = super(Eliminar_Producto, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('listar_productos')
        return context



#CATEGORIAS DE PRODUCTOS ::
class Listado_Categoria(SuccessMessageMixin, ListView):
    model = Category
    template_name = 'servicios/cart/listado_categorias.html'
    def get_queryset(self):
            return Category.objects.all().order_by('id')

class Registrar_Categoria(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'servicios/cart/agregar_categoria.html'
    success_url = reverse_lazy('pagina_categorias')

    def get_context_data(self, **kwargs):  # pinto el formulario en el html
        context = super(Registrar_Categoria, self).get_context_data(**kwargs)
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

#editar ::


class Editar_Categoria(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'servicios/cart/editar_categoria.html'
    def get_context_data(self,**kwargs):
        context = super(Editar_Categoria, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        categoria_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = categoria_editar)
        context['id'] = pk_editar

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        categoria = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = categoria)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse_lazy('pagina_categorias'))
        else:
            return HttpResponseRedirect(reverse_lazy('pagina_categorias'))
#eliminar :
class Eliminar_Categoria(DeleteView):
    model = Category
    template_name =  'servicios/cart/eliminar_categoria.html'
    success_url=reverse_lazy('pagina_categorias')
    def get_context_data(self,**kwargs):

        context = super(Eliminar_Categoria, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('pagina_categorias')
        return context

