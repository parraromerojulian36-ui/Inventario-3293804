from django.urls import path
from . import views

urlpatterns = [
    path('pos/', views.registrar_venta, name='registrar_venta'),
    path('historial/', views.historial_ventas, name='historial_ventas'),
]