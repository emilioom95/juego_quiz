# juego/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('listar_preguntas/', views.listar_preguntas, name='listar_preguntas'),
    path('agregar_pregunta/', views.agregar_pregunta, name='agregar_pregunta'),
    path('editar_pregunta/<int:pk>/', views.editar_pregunta, name='editar_pregunta'),
    path('borrar_pregunta/<int:pk>/', views.borrar_pregunta, name='borrar_pregunta'),
    path('jugar/', views.jugar_view, name='jugar'),
    path('resultado_correcto/', views.resultado_correcto_view, name='resultado_correcto'),
    path('resultado_incorrecto/', views.resultado_incorrecto_view, name='resultado_incorrecto'),
    
]
