from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import Listado_Order,OrderDetail,OrderUpdate,Eliminar_Order
urlpatterns = [
    # !-------------------------- PAGINA  ----------------------------------------

    url(r'^create/$', views.order_create, name='order_create'),
    path('pagina_order/', Listado_Order.as_view(), name='pagina_order'),

    # !-------------------------- ELIMINAR ORDER  ----------------------------------------
    path('delete_order/<int:pk>', Eliminar_Order.as_view(), name='delete_order'),

    # !-------------------------- EDITAR PRODUCTO/CATEGORIA  ----------------------------------------
    path('editar_order/<int:pk>', OrderUpdate.as_view(), name='editar_order'),


    # !-------------------------- DETALLE ORDER  ----------------------------------------
    path('detalle_order/<int:pk>', OrderDetail.as_view(), name='detalle_order'),
]