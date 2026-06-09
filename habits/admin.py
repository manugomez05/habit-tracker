from django.contrib import admin
from .models.persona.model import Persona
from .models.grupo.model import Grupo
from .models.tarea.model import Tarea

admin.site.register(Persona)
admin.site.register(Grupo)
admin.site.register(Tarea)