from django.urls import path
from . import views

urlpatterns = [
    # URLs de Categoría
    path('', views.inicio_PChop, name='inicio'),
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categoria/ver/', views.ver_categorias, name='ver_categorias'),
    path('categoria/actualizar/<int:categoria_id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/borrar/<int:categoria_id>/', views.borrar_categoria, name='borrar_categoria'),
    
    # URLs de Producto
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_productos, name='ver_productos'),
    path('producto/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    
    # NUEVAS URLs de Pedido
    path('pedido/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedido/ver/', views.ver_pedidos, name='ver_pedidos'),
    path('pedido/actualizar/<int:pedido_id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedido/borrar/<int:pedido_id>/', views.borrar_pedido, name='borrar_pedido'),
]