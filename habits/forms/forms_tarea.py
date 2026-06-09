from django import forms

from habits.models.models_tarea import Tarea
from habits.models.models_grupo import Grupo

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            
            'grupo'
        ]
