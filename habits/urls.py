from django.urls import path
from .views import persona
from . import views

urlpatterns = [
    path('',persona),
    path('personas/',persona, name='lista_personas'),
    path('modificar/<int:id>/', views.modificarPersona, name='modificarPersona'),
    path('crear_persona/', crear_persona, name='crear_persona'),
]

