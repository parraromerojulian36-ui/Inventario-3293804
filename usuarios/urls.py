from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('empresa/crear/', views.crear_empresa, name='crear_empresa'),
    path('empresa/editar/<int:id_empresa>/', views.editar_empresa, name='editar_empresa'),
]

