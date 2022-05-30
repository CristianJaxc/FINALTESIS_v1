
from django.urls import path
from .import views
from app.home.views import signup_view
from app.usuario.views import Detalle_usuario, Listado_usuarios,Eliminar_usuario, volunView, Detail_Usu, Mi_Usuario_Update ,quienes_somos

urlpatterns = [
    path('perfilvoluntario/',volunView.as_view(),name='perfil'),
    path('perfilvoluntario/<int:pk>',Detail_Usu.as_view(),name='detalle_perfil'),
    path('editar_mi_usuario/<int:pk>', Mi_Usuario_Update.as_view(), name='editar_volunt'),
    path('eliminar_mi_usuario/<int:pk>', Eliminar_usuario.as_view(), name='eliminar_usuarios'),
    path('listado_usuarios/', Listado_usuarios.as_view(), name='listado_usuarios'),
    path('detalle_usuario/<int:pk>', Detalle_usuario.as_view(), name='detalle_usuario'),
    path('quienes_somos/>',quienes_somos.as_view(), name='quienes_somos'),
 
]


