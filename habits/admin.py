from django.contrib import admin
from .models.models_persona import Persona
from .models.models_grupo import Grupo
from .models.models_tarea import Tarea

admin.site.register(Persona)
admin.site.register(Grupo)
admin.site.register(Tarea)