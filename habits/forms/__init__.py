"""
Consolidación de formularios
"""
from .persona.forms import PersonaForm
from .grupo.forms import GrupoForm
from .tarea.forms import TareaFormCrear, TareaFormEditar
from .usuario.forms import CrearUsuarioPersonaForm

__all__ = ['PersonaForm', 'GrupoForm', 'TareaFormCrear', 'TareaFormEditar', 'CrearUsuarioPersonaForm']
