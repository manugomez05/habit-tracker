from django import forms
from ...models.tarea.model import Tarea
from ...models.persona.model import Persona


def persona_puede_resolver_dificultad(persona, dificultad):
    rol = persona.rol.nombre if persona.rol else None
    if dificultad == Tarea.DIFICULTAD_BAJA:
        return rol in ['Integrante', 'Lider', 'Administrador']
    if dificultad == Tarea.DIFICULTAD_MEDIA:
        return rol in ['Lider', 'Administrador']
    if dificultad == Tarea.DIFICULTAD_ALTA:
        return rol == 'Administrador'
    return False


def roles_permitidos_por_dificultad(dificultad):
    if dificultad == Tarea.DIFICULTAD_MEDIA:
        return ['Lider', 'Administrador']
    if dificultad == Tarea.DIFICULTAD_ALTA:
        return ['Administrador']
    return ['Integrante', 'Lider', 'Administrador']


def personas_disponibles_por_dificultad(dificultad):
    return Persona.objects.filter(rol__nombre__in=roles_permitidos_por_dificultad(dificultad)).order_by('nombre', 'apellido')


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
            'dificultad': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dificultad = self.data.get('dificultad') or self.initial.get('dificultad') or Tarea.DIFICULTAD_BAJA
        self.fields['personas'].queryset = personas_disponibles_por_dificultad(dificultad)

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
            'dificultad': forms.Select(attrs={'class': 'form-select'}),
            'completada': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dificultad = (
            self.data.get('dificultad')
            or self.initial.get('dificultad')
            or getattr(self.instance, 'dificultad', None)
            or Tarea.DIFICULTAD_BAJA
        )
        self.fields['personas'].queryset = personas_disponibles_por_dificultad(dificultad)

    def clean(self):
        cleaned_data = super().clean()
        validar_personas_por_dificultad(cleaned_data)
        return cleaned_data
