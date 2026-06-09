from django import forms
from ...models.persona.model import Persona
from ...models.grupo.model import Grupo


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
