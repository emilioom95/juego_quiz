from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pregunta, Perfil
from .forms import PreguntaForm, RespuestaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
import random
from django.contrib import messages

def agregar_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_preguntas')
    else:
        form = PreguntaForm()
    return render(request, 'preguntas/agregar_pregunta.html', {'form': form})

def editar_pregunta(request, pk):
    pregunta = get_object_or_404(Pregunta, pk=pk)
    if request.method == 'POST':
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('listar_preguntas')
    else:
        form = PreguntaForm(instance=pregunta)
    return render(request, 'preguntas/editar_pregunta.html', {'form': form})

def listar_preguntas(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'preguntas/listar_preguntas.html', {'preguntas': preguntas})

def borrar_pregunta(request, id):
    pregunta = get_object_or_404(Pregunta, id=id)
    if request.method == 'POST':
        pregunta.delete()
        return redirect('listar_preguntas')
    return redirect('listar_preguntas')

def inicio(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('listar_preguntas')  # Redirige al admin a la página de administración de preguntas
        else:
            return redirect('jugar')  # Redirige al usuario normal a la página para jugar
    else:
        return render(request, 'inicio.html')

def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def jugar(request):
    return render(request, 'jugar.html')

def resultado_correcto_view(request):
    return render(request, 'juego/resultado_correcto.html')

def resultado_incorrecto_view(request):
    return render(request, 'juego/resultado_incorrecto.html')

def jugar_view(request):
    user = request.user
    
    try:
        perfil = Perfil.objects.get(user=user)
    except Perfil.DoesNotExist:
        perfil = Perfil.objects.create(user=user)
    
    preguntas = list(Pregunta.objects.all())
    
    if not preguntas:
        return render(request, 'juego/jugar.html', {'mensaje': 'No hay preguntas disponibles.'})

    pregunta_actual = random.choice(preguntas)
    opciones = [pregunta_actual.opcion1, pregunta_actual.opcion2, pregunta_actual.opcion3, pregunta_actual.opcion4]
    
    if request.method == 'POST':
        form = RespuestaForm(request.POST, opciones=opciones)
        if form.is_valid():
            respuesta_elegida = form.cleaned_data['opciones']
            if respuesta_elegida == pregunta_actual.respuesta_correcta:
                perfil.puntos += 10
                perfil.save()
                return redirect('resultado_correcto')
            else:
                return redirect('resultado_incorrecto')
    else:
        form = RespuestaForm(opciones=opciones)
    
    return render(request, 'juego/jugar.html', {
        'pregunta': pregunta_actual,
        'form': form
    })