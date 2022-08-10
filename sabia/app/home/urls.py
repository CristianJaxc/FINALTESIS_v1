from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from app.home.views import signup_view, ContactoCreate,Eliminar_Contacto, Contactos_Listado,\
    ContactoDetail,quienes_somos,ContactoVoluntario

urlpatterns = [
    path('',views.index,name='home' ),
    path('pagina',views.prueba,name='pagina'),
    path('signup/', signup_view, name="signup"),
    path('quienes_somos_contacto', views.quienes_somos, name="quienes_somos_contacto"),
    path('contacto_registrar',ContactoCreate.as_view(),name='contacto_registrar'),
    path('contacto_voluntario', ContactoVoluntario.as_view(), name='contacto_voluntario'),
    path('contacto_listado',Contactos_Listado.as_view(),name='contacto_listado'),
    path('contacto_eliminar/<int:pk>',Eliminar_Contacto.as_view(),name='contacto_eliminar'),
    path('contactos_detalle/<int:pk>', ContactoDetail.as_view(), name='contactos_detalle'),
    path('',include('pwa.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
