from django import forms
from .models.models_persona import Persona
from habits.models.models_grupo import Grupo


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
