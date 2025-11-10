from django.contrib import admin
from .models import Categoria, Producto, Pedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'prioridad', 'fecha_creacion']
    list_filter = ['activa', 'fecha_creacion']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'marca', 'fecha_agregado']
    list_filter = ['categoria', 'marca', 'fecha_agregado']
    search_fields = ['nombre', 'marca']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'total', 'estado', 'metodo_pago', 'fecha_pedido']
    list_filter = ['estado', 'metodo_pago', 'fecha_pedido']
    search_fields = ['cliente']