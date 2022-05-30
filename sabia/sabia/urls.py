"""sabia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import url, include

from django.utils.translation import gettext_lazy as _

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.home.urls')),
    path('usuario/',  include('app.usuario.urls')),
    path('denuncias/',  include('app.denuncias.urls')),
    path('adopciones/',  include('app.adopciones.urls')),
    path('donaciones/',  include('app.donaciones.urls')),
    path('blogs/',  include('app.blogs.urls')),
    #path('servicios/', include('app.servicios.urls')),
    url(r'paypal/', include('paypal.standard.ipn.urls')),
    url(r'payment/',include('app.payment.urls')),
    url('servicios/', include('app.servicios.urls')),
    url(r'^cart/', include('app.cart.urls')),
    url(r'orders/', include('app.orders.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #-----------------cliente
    url('cliente/', include('app.cliente.urls')),
    path('i18n/', include("django.conf.urls.i18n")),
    path('',include('pwa.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

