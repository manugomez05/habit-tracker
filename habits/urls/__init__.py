from django.urls import path, include

# Importar las URLs de cada módulo
from .login import urlpatterns as urlpatterns_login
from .persona.urls import urlpatterns as urlpatterns_persona
from .tarea.urls import urlpatterns as urlpatterns_tarea


# Consolidar todos los patrones de URLs
urlpatterns = []
urlpatterns += urlpatterns_login + urlpatterns_persona + urlpatterns_tarea
