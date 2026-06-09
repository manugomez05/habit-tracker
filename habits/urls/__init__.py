from django.urls import path, include
from django.shortcuts import redirect

# Importar las URLs de cada módulo
from .persona.urls import urlpatterns as urlpatterns_persona
from .grupo.urls import urlpatterns as urlpatterns_grupo
from .tarea.urls import urlpatterns as urlpatterns_tarea


def _root_redirect(request):
	"""Redirige la raíz del site a la lista de personas."""
	return redirect('lista_personas')


# Consolidar todos los patrones de URLs (incluyendo la raíz)
urlpatterns = [
	path('', _root_redirect, name='home'),
]
urlpatterns += urlpatterns_persona + urlpatterns_grupo + urlpatterns_tarea
