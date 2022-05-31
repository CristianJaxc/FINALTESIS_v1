
from django.urls import reverse
from django.shortcuts import render, redirect

from app.cart.cart import Cart
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem,Order
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect
#MENSAJERIA ::
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView


# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
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

        form = OrderCreateForm()

    return render(request, 'servicios/orders/order_create.html',
                  {'cart': cart, 'form': form})


class Listado_Order(SuccessMessageMixin, ListView):
    model = OrderItem
    template_name = 'servicios/orders/listado_order.html'
    def get_queryset(self):
            return OrderItem.objects.all().order_by('id')


#EDITAR / VER MAS DETALLE ORDER :

class OrderDetail(SuccessMessageMixin, TemplateView):
    template_name = 'servicios/orders/detalle_order.html'
    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        Order1 = Order.objects.get(id = pk)
        #print(usuario.username)
        return {'Order1':Order1}



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
    model = OrderItem
    template_name = 'servicios/orders/eliminar_order.html'
    success_url=reverse_lazy('pagina_order')


    def get_context_data(self,**kwargs):
        context = super(Eliminar_Order, self).get_context_data(**kwargs)
        context['action']='eliminar'
        context['list_url']=reverse_lazy('pagina_order')
        return context
