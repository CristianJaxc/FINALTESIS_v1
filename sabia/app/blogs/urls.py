from django.urls import path
from .import views
from app.blogs.views import Listado_blogs,DetalleDeleteView ,Registrar_Blogs, Editar_blogs, Detalle_blogs,Pagina_Noticia

urlpatterns = [
    path('pagina_blogs/',views.Pagina_blogs,name='pagina_blogs'),
    path('pagina_noticia/',views.Pagina_Noticia,name='pagina_noticia'),
    path('listado_blogs/',Listado_blogs.as_view(),name='listado_blogs'),
    path('registrar_blogs/',Registrar_Blogs.as_view(),name='registrar_blogs'),
    path('editar_blogs/<int:pk>', Editar_blogs.as_view(), name='editar_blogs'),
    path('elimina_blogs/<int:pk>', DetalleDeleteView.as_view(), name='eliminar_blogs'),
    path('detalle_blogs/<int:pk>',Detalle_blogs.as_view(),name='detalle_blogs'),
    #path('perfilvoluntario/<int:pk>',Detail_Usu.as_view(),name='detalle_perfil'),
    #path('editar_mi_usuario/<int:pk>', Mi_Usuario_Update.as_view(), name='editar_volunt'),
]


