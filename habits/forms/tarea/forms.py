from django import forms
from ...models.tarea.model import Tarea
from ...models.grupo.model import Grupo

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            'grupo'
        ]
