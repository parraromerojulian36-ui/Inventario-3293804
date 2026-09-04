from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'codigo_barras', 'precio_venta', 'stock_actual', 'estado')
    search_fields = ('nombre_producto', 'codigo_barras')