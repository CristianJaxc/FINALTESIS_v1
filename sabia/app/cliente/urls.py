
from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('register/', views.register, name='register_cliente'),
    path('', views.login, name="login_cliente"),
    path('', views.logouts, name="logout_cliente")

]

