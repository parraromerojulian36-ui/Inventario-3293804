"""
URL configuration for Main project.
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
]
=======
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.home, name='home'),
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('Inventario/', include('Gestion_Inventario.urls')),
    path('ventas/', include('Gestion_Ventas.urls')),
    path('usuarios/', include('Usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 663911e0af3b14d7e689bb5d52b50dbfb673b460
