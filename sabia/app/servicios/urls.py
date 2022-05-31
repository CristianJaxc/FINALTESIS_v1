from django.urls import path
from .import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import pagina_productos,product_list,product_detail,Registrar_Imagenes,Registrar_Producto,Listado_Productos,Eliminar_Producto,Listado_Categoria,Registrar_Categoria,Editar_Producto,Eliminar_Categoria,Editar_Categoria

urlpatterns = [
    #!-------------------------- esterilizacion ----------------------------------------
    path('pagina_esterilizacion/',views.esterilizacion, name='pagina_esterilizacion'),
    # !-------------------------- PAGINA DE SERVICIOS  ----------------------------------------
    path('pagina_productos/', views.pagina_productos, name='pagina_productos'),
    path('pagina_categorias/', Listado_Categoria.as_view(), name='pagina_categorias'),
    # !-------------------------- Añadir PRODUCTO/CATEGORIA  ----------------------------------------
    path('add_categoria/', Registrar_Categoria.as_view(), name='add_categoria'),
    path('add_productos/',Registrar_Producto.as_view(), name='add_productos'),
    path('add_imagenes/<int:pk>',Registrar_Imagenes.as_view(), name='add_imagenes'),

    # !-------------------------- ELIMINAR PRODUCTO/CATEGORIA  ----------------------------------------
    path('delete_producto/<int:pk>', Eliminar_Producto.as_view(), name='delete_producto'),
    path('delete_categoria/<int:pk>', Eliminar_Categoria.as_view(), name='delete_categoria'),

    # !-------------------------- EDITAR PRODUCTO/CATEGORIA  ----------------------------------------
    path('editar_producto/<int:pk>',Editar_Producto.as_view(), name='editar_producto'),
    path('editar_categoria/<int:pk>', Editar_Categoria.as_view(), name='editar_categoria'),

    # !--------------------------LISTADOS   PRODUCTO/CATEGORIA  ----------------------------------------
    path('listaar_productos/', Listado_Productos.as_view(), name='listar_productos'),
    url('product_list', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'payment/',include('app.payment.urls')),

    #path('listado_productos/', views.product_list, name='listados_productos'),
    #path('Detalle_productos/<int:id>', views.product_detail, name='Detalle_productos'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



