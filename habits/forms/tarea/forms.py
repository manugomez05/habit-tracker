from django import forms
from ...models.tarea.model import Tarea

class TareaFormCrear(forms.ModelForm):
    """Formulario para crear tareas - sin campo completada"""
    personas = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.SelectMultiple(attrs={'size': 1, 'class': 'form-select'}),
        label='Asignar a Personas',
        required=False
    )
    
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            'fecha_vencimiento',
            'personas'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título de la tarea'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción', 'rows': 4}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from ...models.persona.model import Persona
        self.fields['personas'].queryset = Persona.objects.all()


class TareaFormEditar(forms.ModelForm):
    """Formulario para editar tareas - con campo completada"""
    personas = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.SelectMultiple(attrs={'size': 1, 'class': 'form-select'}),
        label='Asignar a Personas',
        required=False
    )
    
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            'fecha_vencimiento',
            'completada',
            'personas'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título de la tarea'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción', 'rows': 4}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'completada': forms.CheckboxInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from ...models.persona.model import Persona
        self.fields['personas'].queryset = Persona.objects.all()
