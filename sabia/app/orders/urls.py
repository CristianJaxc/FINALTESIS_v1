from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import Listado_Order,OrderDetail,OrderUpdate,Eliminar_Order,Order_create5,\
    order_create_paypal,Listado_Order1,OrderUpdate_Cliente,OrderDetailCliente
urlpatterns = [
    # !-------------------------- PAGINA  ----------------------------------------

    url(r'^create/$', views.order_create, name='order_create'),
    url(r'order_create_paypal', views.order_create_paypal, name='order_create_paypal'),
    path('pagina_order/', Listado_Order.as_view(), name='pagina_order'),

    # !-------------------------- ELIMINAR ORDER  ----------------------------------------
    path('delete_order/<int:pk>', Eliminar_Order.as_view(), name='delete_order'),

    # !-------------------------- EDITAR PRODUCTO/CATEGORIA  ----------------------------------------
    path('editar_order/<int:pk>', OrderUpdate.as_view(), name='editar_order'),
    path('editar_order_cliente/<int:pk>', OrderUpdate_Cliente.as_view(), name='editar_order_cliente'),

    path('detalle_order_cliente/<int:pk>', OrderDetailCliente.as_view(), name='detalle_order_cliente'),

    # !-------------------------- DETALLE ORDER  ----------------------------------------
    path('detalle_order/<int:pk>', OrderDetail.as_view(), name='detalle_order'),
    path('detalle_order5/',    Order_create5.as_view(), name='detalle_order5'),
    path('estado_pedido1/', Listado_Order1.as_view(), name='estado_pedido1'),
    # !-------------------------- Login  ----------------------------------------



]