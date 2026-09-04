from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from .models import Venta, DetalleVenta
from Gestion_Inventario.models import Producto

def registrar_venta(request):
    productos = Producto.objects.filter(estado='ACTIVO', stock_actual__gt=0)
    
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))
        cliente = request.POST.get('cliente_nombre', 'Cliente General')
        metodo = request.POST.get('metodo_pago', 'EFECTIVO')

        producto = get_object_or_404(Producto, id=producto_id)

        # Acá qqueremos validar que haya sckock suficiente antes de realizar la venta
        if producto.stock_actual < cantidad:
            messages.error(request, f"Stock insuficiente para {producto.nombre_producto}. Disponible: {producto.stock_actual}")
            return redirect('registrar_venta')

        try:
            with transaction.atomic():
                # 1. Crear registro de venta
                subtotal = producto.precio_venta * cantidad
                nueva_venta = Venta.objects.create(
                    vendedor=request.user,
                    cliente_nombre=cliente,
                    metodo_pago=metodo,
                    total=subtotal
                )

                # 2. Guardardo los detalles de cada ítems de las ventas
                DetalleVenta.objects.create(
                    venta=nueva_venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio_venta,
                    subtotal=subtotal
                )

                # 3. Cuando quiero descargar el inventario
                producto.stock_actual -= cantidad
                producto.save()

                messages.success(request, f"Venta #{nueva_venta.id} registrada e inventario actualizado.")
                return redirect('historial_ventas')

        except Exception as e:
            messages.error(request, f"Error al procesar la venta: {str(e)}")

    return render(request, 'Ventas/home.html', {'productos': productos})

def historial_ventas(request):
    ventas = Venta.objects.prefetch_related('detalles__producto').order_by('-fecha_venta')
    return render(request, 'Ventas/historial.html', {'ventas': ventas})