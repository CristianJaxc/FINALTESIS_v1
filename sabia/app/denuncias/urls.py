from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from app.denuncias.views import Denuncias_Listado, DenuciaCreate, DenunciaDetail, DenunciaUpdate,Eliminar_denuncia

urlpatterns = [
    path('denunciaslistado',Denuncias_Listado.as_view(),name='denuncias_listado'),
    path('pagina_denuncias',views.Pagina_denuncias, name='pagina_denuncias'),
    path('denuncias_registrar',DenuciaCreate.as_view(),name='denuncias_registrar'),
    path('denuncias_detalle/<int:pk>', DenunciaDetail.as_view(), name='denuncias_detalle'),
    path('denuncias_update/<int:pk>', DenunciaUpdate.as_view(), name='denuncias_update'),
    path('denuncias_eliminar/<int:pk>',Eliminar_denuncia.as_view(), name='denuncias_eliminar'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




