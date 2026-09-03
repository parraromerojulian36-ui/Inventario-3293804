from django.urls import path
from .views import home_inventario

app_name = 'Gestion_Inventario'


urlpatterns = [
    path('', home_inventario, name='home_inventario'),
]
