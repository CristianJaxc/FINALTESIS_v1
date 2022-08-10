from django.urls import path
from .import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import reportVentas,reporteProductos,reportGrafico,reportDenuncia,reportAdopciones,reportDonaciones

urlpatterns = [
    #!-------------------------- esterilizacion ----------------------------------------
    path('reportes_ventas/',reportVentas.as_view(), name='reportes_ventas'),
    path('reportes_productos/',reporteProductos.as_view(), name='reportes_productos'),
    path('reporte_grafico/', reportGrafico.as_view(), name='reporte_grafico'),
    path('reporte_denuncia/', reportDenuncia.as_view(), name='reporte_denuncia'),
    path('reporte_adopciones/', reportAdopciones.as_view(), name='reporte_adopciones'),
    path('reporte_donaciones/', reportDonaciones.as_view(), name='reporte_donaciones'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)