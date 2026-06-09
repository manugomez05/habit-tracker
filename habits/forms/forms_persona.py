from django import forms
from .models.models_persona import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellido',
            'documento'
        ]
