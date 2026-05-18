from django import forms
from .models import Persona, Grupo

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellido',
            'documento'
        ]

class GrupoForm(forms.ModelForm):
    miembros = forms.ModelMultipleChoiceField(
        queryset=Persona.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Grupo
        fields = [
            'nombre',
            'miembros'
        ]
