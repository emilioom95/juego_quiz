from django.contrib import admin
from django.urls import path, include
from juego import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Incluye URLs de autenticación
    path('register/', views.registrarse, name='registrarse'),
    path('', views.inicio, name='inicio'),  # Ruta para la vista de inicio
    path('juego/', include('juego.urls')),  # Incluye URLs de la aplicación juego
]