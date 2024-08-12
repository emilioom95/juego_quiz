from django import forms
from .models import Pregunta

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['pregunta', 'opcion1', 'opcion2', 'opcion3', 'opcion4', 'respuesta_correcta']

class RespuestaForm(forms.Form):
    opciones = forms.ChoiceField(choices=[], widget=forms.RadioSelect)
    
    def __init__(self, *args, **kwargs):
        # Extrae las opciones del kwargs, con valor predeterminado como lista vacía
        opciones = kwargs.pop('opciones', [])
        super().__init__(*args, **kwargs)
        # Asigna las opciones al campo 'opciones' del formulario
        self.fields['opciones'].choices = [(opcion, opcion) for opcion in opciones]