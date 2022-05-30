from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from app.adopciones.views import PerroCreate, PerroDetail,Eliminar_Solicitud,Eliminar_Perro, PerroUpdate, SolicitudDetail, SolicitudUpdate, adopciones_Listado, Perro_Listado, SolicitudCreate

urlpatterns = [
    path('adopcioneslistado/',adopciones_Listado.as_view(),name='adopciones_listado'),
    path('adopcionesEliminar/<int:pk>',Eliminar_Solicitud.as_view(),name='eliminar_solicitud'),
    path('pagina_adopciones/',views.Pagina_adopciones, name='pagina_adopciones'),
    # path('pagina_adopciones/',pagina_adopciones.as_view(), name='pagina_adopciones'),
    path('registrar_solicitud/<int:pk>',SolicitudCreate.as_view(),name='registrar_solicitud'),
    path('detalle_solicitud/<int:pk>', SolicitudDetail.as_view(), name='detalle_solicitud'),
    path('editar_solicitud/<int:pk>', SolicitudUpdate.as_view(), name='editar_solicitud'),
    #!----------------------- Perro ---------------------------------------
    path('registrar_perro/',PerroCreate.as_view(),name='registrar_perro'),
    path('listado_perro/',Perro_Listado.as_view(),name='listado_perro'),
    path('detalle_perro/<int:pk>', PerroDetail.as_view(), name='detalle_perro'),
    path('editar_perro/<int:pk>', PerroUpdate.as_view(), name='editar_perro'),
    path('eliminar_perro/<int:pk>',Eliminar_Perro.as_view(), name='eliminar_perro'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


