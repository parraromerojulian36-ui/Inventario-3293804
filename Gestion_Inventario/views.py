from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from .models import Producto
from .serializer import ProductoSerializer

def home_inventario(request):
    productos = Producto.objects.all()
    return render(request, 'Inventario/home.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        Producto.objects.create(
            codigo_barras=request.POST.get('codigo_barras'),
            sku_interno=request.POST.get('sku_interno'),
            fecha_vencimiento=request.POST.get('fecha_vencimiento') or None,
            nombre_producto=request.POST.get('nombre_producto'),
            categoria=request.POST.get('categoria'),
            marca_modelo=request.POST.get('marca_modelo'),
            descripcion=request.POST.get('descripcion'),
            precio_venta=request.POST.get('precio_venta') or 0,
            costo_adquisicion=request.POST.get('costo_adquisicion') or 0,
            stock_actual=request.POST.get('stock_actual') or 0,
            stock_minimo=request.POST.get('stock_minimo') or 0,
            ubicacion_bodega=request.POST.get('ubicacion_bodega'),
            unidad_medida=request.POST.get('unidad_medida'),
            estado=request.POST.get('estado'),
        )
        messages.success(request, '¡Producto creado con éxito!')
        return redirect('Gestion_Inventario:home_inventario')
    
    return render(request, 'Inventario/crear_producto.html')

def editar_producto(request, sku_interno):
    producto_obj = get_object_or_404(Producto, sku_interno=sku_interno)
    
    if request.method == 'POST':
        producto_obj.codigo_barras = request.POST.get('codigo_barras')
        producto_obj.sku_interno = request.POST.get('sku_interno')
        producto_obj.fecha_vencimiento = request.POST.get('fecha_vencimiento') or None
        producto_obj.nombre_producto = request.POST.get('nombre_producto')
        producto_obj.categoria = request.POST.get('categoria')
        producto_obj.marca_modelo = request.POST.get('marca_modelo')
        producto_obj.descripcion = request.POST.get('descripcion')
        producto_obj.precio_venta = request.POST.get('precio_venta')
        producto_obj.costo_adquisicion = request.POST.get('costo_adquisicion')
        producto_obj.stock_actual = request.POST.get('stock_actual')
        producto_obj.stock_minimo = request.POST.get('stock_minimo')
        producto_obj.ubicacion_bodega = request.POST.get('ubicacion_bodega')
        producto_obj.unidad_medida = request.POST.get('unidad_medida')
        producto_obj.estado = request.POST.get('estado')
        producto_obj.save()
        
        messages.success(request, '¡Los datos del Producto han sido actualizados con éxito!')
        return redirect('Gestion_Inventario:home_inventario')
        
    return render(request, 'usuarios/empresa_forms.html', {'producto': producto_obj})

def eliminar_producto(request, sku_interno):
    producto_obj = get_object_or_404(Producto, sku_interno=sku_interno)
    
    if request.method == 'POST':
        producto_obj.delete()
        messages.success(request, 'Producto Eliminado.')
        return redirect('Gestion_Inventario:home_inventario')
        
    return render(request, 'Inventario/confirmar_eliminar.html', {'producto': producto_obj})


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

