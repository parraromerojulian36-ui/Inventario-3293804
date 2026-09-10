from django.db import models

class Sede(models.Model):
    nombreSede = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    estado = models.BooleanField(default=True)