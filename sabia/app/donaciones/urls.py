from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from app.donaciones.views import editar_solicitud_donacion,Solicitud_detalle_donacion,Eliminar_solicitud, Eliminar_donacion, Solicitud_donacion, Listado_Solicitudes_donaciones, Listado_donaciones, Registrar_Producto, Editar_Producto


urlpatterns = [
    #!-------------------------- donaciones ----------------------------------------
    path('pagina_donaciones/',views.Pagina_donaciones, name='pagina_donaciones'),
    path('listado_donaciones/',Listado_donaciones.as_view(),name='listado_donaciones'),
    path('registrar_producto/',Registrar_Producto.as_view(),name='registrar_producto'),
    path('editar_producto/<int:pk>', Editar_Producto.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:pk>', Eliminar_donacion.as_view(), name='eliminar_producto'),
    # !-------------------------- APADRINAMIENTO : ----------------------------------------
    path('pagina_apadrinamiento/', views.Pagina_apdrinamiento, name='pagina_apadrinamiento'),


    #!-------------------------- Solicitudes ---------------------------------------
    path('listado_solicitudes_donaciones/',Listado_Solicitudes_donaciones.as_view(),name='listado_solicitudes_donaciones'),
    path('registrar_solicitud_donacion/<int:pk>',Solicitud_donacion.as_view(),name='registrar_solicitud_donacion'),
    path('detalle_solicitud_donacion/<int:pk>', Solicitud_detalle_donacion.as_view(), name='detalle_solicitud_donacion'),
    path('editar_solicitud_donacion/<int:pk>', editar_solicitud_donacion.as_view(), name='editar_solicitud_donacion'),
    path('eliminar_solicitud_donacion/<int:pk>', Eliminar_solicitud.as_view(), name='eliminar_solicitud_donacion'),
    #!-------------------------- otros ---------------------------------------------
    #path('adopcioneslistado/',adopciones_Listado.as_view(),name='adopciones_listado'),
    #path('pagina_adopciones/',views.Pagina_adopciones, name='pagina_adopciones'),
    #path('registrar_solicitud/<int:pk>',SolicitudCreate.as_view(),name='registrar_solicitud'),
    #path('detalle_solicitud/<int:pk>', SolicitudDetail.as_view(), name='detalle_solicitud'),
    #path('editar_solicitud/<int:pk>', SolicitudUpdate.as_view(), name='editar_solicitud'),
    #!----------------------- Perro ---------------------------------------
    #path('registrar_perro/',PerroCreate.as_view(),name='registrar_perro'),
    #path('listado_perro/',Perro_Listado.as_view(),name='listado_perro'),
    #path('detalle_perro/<int:pk>', PerroDetail.as_view(), name='detalle_perro'),
    #path('editar_perro/<int:pk>', PerroUpdate.as_view(), name='editar_perro'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







