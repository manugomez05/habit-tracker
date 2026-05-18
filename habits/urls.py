from django.urls import path
from .views import (
    persona,
    crear_persona,)

urlpatterns = [
    path('personas/',persona, name='lista_personas'),

    path('crear_persona/', crear_persona, name='crear_persona'),
]
