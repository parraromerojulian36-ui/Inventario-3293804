from django.urls import path
from . import views

app_name = 'Usuarios'


urlpatterns = [
    path('', views.home, name='home'),
    path('empresa/', views.datos_empresa, name='datos_empresa'),
    path('sedes/', views.lista_sedes, name='lista_sedes'),
    path('sedes/nueva/', views.crear_sede, name='crear_sede'),
    path('sedes/editar/<int:id>/', views.editar_sede, name='editar_sede'),
    path('sedes/eliminar/<int:id>/', views.eliminar_sede, name='eliminar_sede'),
]
