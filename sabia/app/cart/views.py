from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

#MENSAJERIA ::
from django.contrib import messages
from app.servicios.models import Product

from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],update_quantity=cd['update'])

        if cd['quantity'] > product.stock:
            cart_product_form = CartAddProductForm()
            cart = Cart(request)
            cart.remove(product)
            messages.success(request, "Supera el Stock")
            return render(request, 'servicios/detalle_productos.html',
                          {'product': product, 'cart_product_form': cart_product_form})
        else:

             return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.error(request, "Producto Eliminado")
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True})

    return render(request, 'servicios/cart/cart_detail.html', {'cart': cart})


