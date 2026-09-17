"""
URL configuration for Main project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.home, name='home'),
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('Inventario/', include('Gestion_Inventario.urls')),
    path('ventas/', include('Gestion_Ventas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('AppTest/', include('AppTest.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)