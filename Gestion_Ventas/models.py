from django.db import models
from django.contrib.auth.models import User
from Gestion_Inventario.models import Producto

class Venta(models.Model):
    METODO_PAGO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia / Nequi / PSE'),
    ]

    vendedor = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    cliente_nombre = models.CharField(max_length=150, default="Cliente General")
    cliente_documento = models.CharField(max_length=20, blank=True, null=True)
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES, default='EFECTIVO')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Factura #{self.id} - {self.fecha_venta.strftime('%Y-%m-%d %H:%M')}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre_producto} (Venta #{self.venta.id})"