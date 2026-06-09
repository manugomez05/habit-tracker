"""
Consolidación de serializadores
"""
from .persona.serializers import PersonaSerializer
from .grupo.serializers import GrupoSerializer
from .tarea.serializers import TareaSerializer

__all__ = ['PersonaSerializer', 'GrupoSerializer', 'TareaSerializer']
