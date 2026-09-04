from django.db import models

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    codigo_barras = models.CharField(max_length=100, unique=True, db_index=True)
    sku_interno = models.CharField(max_length=50, unique=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    nombre_producto = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    marca_modelo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2)
    costo_adquisicion = models.DecimalField(max_digits=12, decimal_places=2)
    stock_actual = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=5)
    ubicacion_bodega = models.CharField(max_length=100, blank=True, null=True)
    unidad_medida = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ACTIVO')

    def __str__(self):
        return f"{self.nombre_producto} ({self.codigo_barras})"