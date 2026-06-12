from django import forms
from ...models.tarea.model import Tarea


def persona_puede_resolver_dificultad(persona, dificultad):
    rol = persona.rol.nombre if persona.rol else None
    if dificultad == Tarea.DIFICULTAD_BAJA:
        return rol in ['Integrante', 'Lider', 'Administrador']
    if dificultad == Tarea.DIFICULTAD_MEDIA:
        return rol in ['Lider', 'Administrador']
    if dificultad == Tarea.DIFICULTAD_ALTA:
        return rol == 'Administrador'
    return False


def validar_personas_por_dificultad(cleaned_data):
    dificultad = cleaned_data.get('dificultad')
    personas = cleaned_data.get('personas')

    if not dificultad or not personas:
        return

    personas_invalidas = [
        persona
        for persona in personas
        if not persona_puede_resolver_dificultad(persona, dificultad)
    ]
    if personas_invalidas:
        nombres = ', '.join(str(persona) for persona in personas_invalidas)
        raise forms.ValidationError(
            f'Estas personas no pueden resolver tareas de dificultad {dificultad}: {nombres}.'
        )


class TareaFormCrear(forms.ModelForm):
    """Formulario para crear tareas - sin campo completada."""
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
            'dificultad',
            'personas'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Titulo de la tarea'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripcion', 'rows': 4}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'dificultad': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from ...models.persona.model import Persona
        self.fields['personas'].queryset = Persona.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        validar_personas_por_dificultad(cleaned_data)
        return cleaned_data


class TareaFormEditar(forms.ModelForm):
    """Formulario para editar tareas - con campo completada."""
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
            'dificultad',
            'completada',
            'personas'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Titulo de la tarea'}),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripcion', 'rows': 4}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'dificultad': forms.Select(),
            'completada': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from ...models.persona.model import Persona
        self.fields['personas'].queryset = Persona.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        validar_personas_por_dificultad(cleaned_data)
        return cleaned_data
