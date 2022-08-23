
from django.urls import path
from django.conf.urls import url

from . import views
from .views import estadoPedido

from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', views.register, name='register_cliente'),
    path('', views.login, name="login_cliente"),
    path('', views.logouts, name="logout_cliente"),
#-----------------------modulos de cliente -------------

#-----------------------Pedido Estado :  cliente -------------
    url('estado_pedido', views.estadoPedido, name='estado_pedido'),


]

