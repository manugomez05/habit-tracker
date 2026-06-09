"""
Consolidación de vistas
"""
from .persona.views import persona, verPersona, crearPersona, modificarPersona, eliminarPersona
from .grupo.views import grupo, verGrupo, crearGrupo, modificarGrupo, eliminarGrupo
from .tarea.views import tareas, verTarea, crearTarea, modificarTarea, eliminarTarea

__all__ = [
    'persona', 'verPersona', 'crearPersona', 'modificarPersona', 'eliminarPersona',
    'grupo', 'verGrupo', 'crearGrupo', 'modificarGrupo', 'eliminarGrupo',
    'tareas', 'verTarea', 'crearTarea', 'modificarTarea', 'eliminarTarea',
]
