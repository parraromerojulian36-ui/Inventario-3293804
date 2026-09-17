from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ventarest', views.VentaViewSet)

app_name = 'Gestion_Ventas'

urlpatterns = [
    path('pos/', views.registrar_venta, name='registrar_venta'),
    path('historial/', views.historial_ventas, name='historial_ventas'),
    path('', include(router.urls)),
]