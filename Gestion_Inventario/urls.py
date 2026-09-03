from django.urls import path
from .views import home_inventario

urlpatterns = [
    path('', home_inventario, name='home_inventario'),
]