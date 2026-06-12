"""
Consolidación de modelos
"""
from .persona.model import Persona
from .grupo.model import Grupo
from .tarea.model import Tarea
from .usuario.model import Usuario
from .rol.model import Rol

__all__ = ['Persona', 'Grupo', 'Tarea', 'Usuario', 'Rol']
