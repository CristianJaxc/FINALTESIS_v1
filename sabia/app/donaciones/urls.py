from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from app.donaciones.views import editar_solicitud_donacion,Solicitud_detalle_donacion,Eliminar_solicitud, Eliminar_donacion, Solicitud_donacion, Listado_Solicitudes_donaciones, Listado_donaciones, Registrar_Producto, Editar_Producto1


urlpatterns = [
    #!-------------------------- donaciones ----------------------------------------
    path('pagina_donaciones/',views.Pagina_donaciones, name='pagina_donaciones'),
    path('listado_donaciones/',Listado_donaciones.as_view(),name='listado_donaciones'),
    path('registrar_producto/',Registrar_Producto.as_view(),name='registrar_producto'),
    path('editar_producto1/<int:pk>',Editar_Producto1.as_view(), name='editar_producto1'),
    path('eliminar_producto/<int:pk>', Eliminar_donacion.as_view(), name='eliminar_producto'),
    # !-------------------------- APADRINAMIENTO : ----------------------------------------
    path('pagina_apadrinamiento/', views.Pagina_apdrinamiento, name='pagina_apadrinamiento'),


    #!-------------------------- Solicitudes ---------------------------------------
    path('listado_solicitudes_donaciones/',Listado_Solicitudes_donaciones.as_view(),name='listado_solicitudes_donaciones'),
    path('registrar_solicitud_donacion/<int:pk>',Solicitud_donacion.as_view(),name='registrar_solicitud_donacion'),
    path('detalle_solicitud_donacion/<int:pk>', Solicitud_detalle_donacion.as_view(), name='detalle_solicitud_donacion'),
    path('editar_solicitud_donacion/<int:pk>', editar_solicitud_donacion.as_view(), name='editar_solicitud_donacion'),
    path('eliminar_solicitud_donacion/<int:pk>', Eliminar_solicitud.as_view(), name='eliminar_solicitud_donacion'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







