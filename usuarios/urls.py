from django.urls import path
from . import views

app_name = 'usuarios'


urlpatterns = [
    path('', views.home, name='home'),
    path('empresa/', views.datos_empresa, name='datos_empresa'),
]
