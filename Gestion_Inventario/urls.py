from django.urls import path, include
from rest_framework import routers
from .views import home_inventario, ProductoViewSet
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

app_name = 'Gestion_Inventario'

router = routers.DefaultRouter()
router.register(r'ProductoApi', ProductoViewSet)

urlpatterns = [
    path('', home_inventario, name='home_inventario'),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
