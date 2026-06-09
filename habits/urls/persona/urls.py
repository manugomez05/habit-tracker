from django.urls import path
from ...views.persona.views import persona, verPersona, modificarPersona, crearPersona, eliminarPersona

urlpatterns = [
    path('personas/', persona, name='lista_personas'),
    path('personas/<int:id>/', verPersona, name='verPersona'),
    path('modificar_persona/<int:id>/', modificarPersona, name='modificarPersona'),
    path('crear_persona/', crearPersona, name='crearPersona'),
    path('eliminar_persona/<int:id>/', eliminarPersona, name='eliminarPersona'),
]
