"""
URL configuration for Main project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login_alt'),
    path('home/', views.home, name='home'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('Inventario/', include('Gestion_Inventario.urls')),
    path('ventas/', include('Gestion_Ventas.urls')),
    path('Usuarios/', include('Usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
