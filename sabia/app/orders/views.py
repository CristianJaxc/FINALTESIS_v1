from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect

from app.cart.cart import Cart
from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.views.decorators.csrf import csrf_exempt

from .forms import OrderCreateForm,OrderCreatePaypalForm
from .models import OrderItem,Order
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect
from app.usuario.forms import PerfilFormVoluntario
from django.contrib.auth.models import User
from app.blogs.models import Blogs
from app import usuario
from app.usuario.models import Perfil
# ---------- Para Formularios -------------
from app.usuario.forms import PerfilForm, UpdateUserForm,PerfilFormVoluntario
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
#MENSAJERIA ::
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView

from random import randint
class Order_create5(SuccessMessageMixin, TemplateView):

    model = User
    second_model = Perfil
    template_name = 'servicios/orders/order_create.html'

    form_class = UpdateUserForm
    second_form_class = PerfilFormVoluntario
    def get_context_data(self, **kwargs):

        context = super(Order_create5, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        pk = self.kwargs.get('pk', 0)
        usuario =User.get.session['order_id']

        # ------------------ obtengo id url -------------------
        usuario_editar = self.model.objects.get(id=pk_editar)
        usuario_editar_perfil = self.second_model.objects.get(User_id=usuario_editar.id)
        perfil = Perfil.objects.get(User_id=usuario.id)
        # print(usuario_editar.id,'aca el otro',usuario_editar_perfil.id)
        # ----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(self.request.FILES, instance=usuario_editar)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.FILES, instance=usuario_editar_perfil)
        context['id'] = pk_editar
        return {'usuario': usuario, 'perfil': perfil, 'context': context}

    def post(self, request, *args, **kwargs):
            cart = Cart(request)

            id_user = kwargs['pk']
            user2 = self.model.objects.get(id=id_user)
            usuario2 = self.second_model.objects.get(User_id=user2.id)
            form = self.form_class(request.POST, request.FILES, instance=user2)
            form2 = self.second_form_class(request.POST, request.FILES, instance=usuario2)
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                for item in cart:
                        order = form2.save()
                        OrderItem.objects.create(order=order, product=item['product'],
                                                 price=item['price'],
                                                 quantity=item['quantity'])

                # clear the cart
                cart.clear()
                # return render(request, 'servicios/orders/order_created.html',
                #    {'order': order})
                # launch asynchronous task

                # set the order in the session
                request.session['order_id'] = order.id
                # redirect to the payment
                return redirect(reverse('process'))

            return render(request, 'servicios/orders/order_create.html',
                          {'cart': cart, 'form': form,',form2': form2})

# Create your views here paypal .
def order_create_paypal(request):
    cart = Cart(request)
    model= Perfil
    if request.method == 'POST':
        voluntario3 = request.user.perfil.role
        form = OrderCreatePaypalForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order = form.save()
            for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                # clear the cart
            cart.clear()
           # return render(request, 'servicios/orders/order_created.html',
                      #    {'order': order})
            # launch asynchronous task

            # set the order in the session
            request.session['order_id'] = order.id
            # redirect to the payment
            return redirect(reverse('process'))
    else:

        form = OrderCreatePaypalForm()

    return render(request, 'servicios/orders/order_create_paypal.html',
                  {'cart': cart, 'form': form})


# Create your views here.
def order_create(request):
    cart = Cart(request)
    form5 = UserCreationForm(request.POST)
    model = Perfil
    form6= PerfilFormVoluntario

    if form5.is_valid() :
        form5.save()
        username = form5.cleaned_data.get('username')
        password = form5.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        #return redirect('perfil')
        a = user.id
        id_usu =user.id  # usuario logeado
        form6 = form6(request.POST, request.FILES)

        if form6.is_valid():
            new = form6.save(commit=False)
            new.User_id = id_usu
            form6.save()
            return redirect('pagina')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST,request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                order = form.save(commit=False)
                order.user = request.user
                order = form.save()
            else :

                order = form.save()

            for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                # clear the cart
            cart.clear()
           # return render(request, 'servicios/orders/order_created.html',
                      #    {'order': order})
            # launch asynchronous task

            # set the order in the session
            request.session['order_id'] = order.id

            # redirect to the payment
            return redirect(reverse('done'))

    else:

        form = OrderCreateForm()

    return render(request, 'servicios/orders/order_create.html',
                  {'cart': cart, 'form': form,'form5': form5,'form6':form6})




class Listado_Order(SuccessMessageMixin, ListView):
    model = Order
    template_name = 'servicios/orders/listado_order.html'
    def get_queryset(self):
            return Order.objects.all().order_by('id')


#EDITAR / VER MAS DETALLE ORDER :

class OrderDetail(SuccessMessageMixin, TemplateView):

    template_name = 'servicios/orders/detalle_order.html'
    def get_context_data(self, **kwargs):

        model = OrderItem
        context = super(OrderDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        Order1 = Order.objects.get(id = pk)
        #Order2 = OrderItem.objects.get(id= Order1.id)
        Order2 = Order.objects.filter(id=Order1.id)
        Order3= OrderItem.objects.all().order_by('id')

        #print(usuario.username)
        return {'Order1':Order1,'Order2':Order2,'Order3':Order3}



class OrderUpdate(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'servicios/orders/editar_order.html'

    def get_context_data(self,**kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        order_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = order_editar)
        context['id'] = pk_editar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        orderselect = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = orderselect)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('detalle_order', kwargs=kwargs))
        else:
            return HttpResponseRedirect(reverse_lazy('detalle_order', kwargs=kwargs))

class Eliminar_Order(DeleteView):
    model = Order
    template_name = 'servicios/orders/eliminar_order.html'
    success_url=reverse_lazy('pagina_order')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_Order, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('pagina_order')
        return context

class Listado_Order1(SuccessMessageMixin, ListView):
    model = Order
    template_name = 'cliente/admin_cliente/estado_pedido.html'

    def get_queryset(self):

        return  Order.objects.all().order_by('id')


class OrderUpdate_Cliente(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'cliente/admin_cliente/editar_ordercliente.html'
    success_url = reverse_lazy('estado_pedido1')
    def get_context_data(self,**kwargs):
        context = super(OrderUpdate_Cliente, self).get_context_data(**kwargs)
        pk_editar = self.kwargs.get('pk', 0)
        #------------------ obtengo id url -------------------
        order_editar = self.model.objects.get(id = pk_editar)
        #----------------- consulta de datos -----------------
        if 'form' not in context:
            context['form'] = self.form_class(instance = order_editar)
        context['id'] = pk_editar
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_editar = kwargs['pk']
        orderselect = self.model.objects.get(id = id_editar)
        form = self.form_class(request.POST, request.FILES, instance = orderselect)
        if form.is_valid():
            form.save()
            return redirect(reverse('estado_pedido1'))
        else:
            return redirect(reverse('estado_pedido1'))



class OrderDetailCliente(SuccessMessageMixin, TemplateView):

    template_name =  'cliente/admin_cliente/detalle_ordercliente.html'
    def get_context_data(self, **kwargs):

        model = OrderItem
        context = super(OrderDetailCliente, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        Order1 = Order.objects.get(id = pk)
        #Order2 = OrderItem.objects.get(id= Order1.id)
        Order2 = Order.objects.filter(id=Order1.id)
        Order3= OrderItem.objects.all().order_by('id')

        #print(usuario.username)
        return {'Order1':Order1,'Order2':Order2,'Order3':Order3}


