
from django.urls import reverse
from django.shortcuts import render, redirect

from app.cart.cart import Cart
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem



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


