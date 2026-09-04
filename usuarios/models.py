from django.db import models

# Create your models here.

class Empresa(models.Model):
    # Opciones para los campos con listas desplegables o radio buttons
    TIPO_RAZON_CHOICES = [
        ('persona', 'Es persona'),
        ('empresa', 'Empresa'),
    ]
    
    TIPO_DOC_CHOICES = [
        ('NIT', 'NIT'),
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
    ]

    # Campos que corresponden al formulario
    tipo_razon_social = models.CharField(max_length=10, choices=TIPO_RAZON_CHOICES, default='empresa')
    razon_social = models.CharField(max_length=200)
    serial = models.CharField(max_length=100)
    tipo_identificacion = models.CharField(max_length=5, choices=TIPO_DOC_CHOICES, default='NIT')
    identificacion = models.CharField(max_length=20)
    dv = models.CharField(max_length=1, blank=True, null=True, verbose_name="Dígito Verificación")
    correo = models.EmailField()
    direccion = models.CharField(max_length=255, blank=True, null=True)
    contacto = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.razon_social