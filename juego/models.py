from django.db import models
from django.contrib.auth.models import User

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    opcion1 = models.CharField(max_length=255)
    opcion2 = models.CharField(max_length=255)
    opcion3 = models.CharField(max_length=255)
    opcion4 = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=255)

    def __str__(self):
        return self.pregunta

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username