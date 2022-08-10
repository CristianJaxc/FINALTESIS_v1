from django.urls import path
from .import views
from app.blogs.views import Listado_blogs,DetalleDeleteView ,Registrar_Blogs,\
    Editar_blogs, Detalle_blogs,Pagina_Noticia,Registrar_Noticia, Listado_Noticias,NotiUpdate, Eliminar_Noticia,\
    Listado_Noticias_blogs,Registrar_Noticia_blogs,Noti_blog_Update,Eliminar_Noticia_blog,Pagina_blogs


urlpatterns = [
    #path('pagina_blogs/',views.Pagina_blogs,name='pagina_blogs'),
    path('pagina_noticia/',views.Pagina_Noticia,name='pagina_noticia'),
    path('listado_blogs/',Listado_blogs.as_view(),name='listado_blogs'),
    path('registrar_blogs/',Registrar_Blogs.as_view(),name='registrar_blogs'),
    path('pagina_blogs/', Pagina_blogs.as_view(), name='pagina_blogs'),
    path('editar_blogs/<int:pk>', Editar_blogs.as_view(), name='editar_blogs'),
    path('elimina_blogs/<int:pk>', DetalleDeleteView.as_view(), name='eliminar_blogs'),
    path('detalle_blogs/<int:pk>',Detalle_blogs.as_view(),name='detalle_blogs'),
    #path('perfilvoluntario/<int:pk>',Detail_Usu.as_view(),name='detalle_perfil'),
    #path('editar_mi_usuario/<int:pk>', Mi_Usuario_Update.as_view(), name='editar_volunt'),

#-------------------------------NOTICIA ------------------------------
    path('registrar_noticia', Registrar_Noticia.as_view(), name='registrar_noticia'),
    path('listado_noticia', Listado_Noticias.as_view(), name='listado_noticia'),
    path('editar_noticia/<int:pk>', NotiUpdate.as_view(), name='editar_noticia'),
    path('eliminar_noticia/<int:pk>', Eliminar_Noticia.as_view(), name='eliminar_noticia'),

#-------------------------------NOTICIA BLOG  ------------------------------
    path('listado_noticia_blogs', Listado_Noticias_blogs.as_view(), name='listado_noticia_blogs'),
    path('registrar_noticia_blogs', Registrar_Noticia_blogs.as_view(), name='registrar_noticia_blogs'),
    path('editar_noticia_blog/<int:pk>', Noti_blog_Update.as_view(), name='editar_noticia_blog'),
    path('eliminar_noticia_blog/<int:pk>', Eliminar_Noticia_blog.as_view(), name='eliminar_noticia_blog'),
]

