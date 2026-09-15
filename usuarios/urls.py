from django.urls import path,include
from . import views
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



app_name = 'usuarios'

router = routers.DefaultRouter()
router.register(r'usuariosrest', views.UsuarioViewSet)
router.register(r'empresasrest', views.EmpresaViewSet, basename='empresasrest')

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_empresa/', views.crear_empresa, name='crear_empresa'),
    path('empresa/editar/<int:id_empresa>/', views.editar_empresa, name='editar_empresa'),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='usuarios:schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='usuarios:schema'), name='redoc'),
]

