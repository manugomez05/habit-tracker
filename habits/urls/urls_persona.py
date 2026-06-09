
from .views.views_persona import persona, verPersona, modificarPersona, crearPersona, eliminarPersona
from . import views
from django.urls import path
urlpatterns = [
path('personas/',persona, name='lista_personas'),
    path('personas/<int:id>/', views.verPersona, name='verPersona'),
    path('modificar_persona/<int:id>/', views.modificarPersona, name='modificarPersona'),
    path('crear_persona/', views.crearPersona, name='crearPersona'),
    path('eliminar_persona/<int:id>/', views.eliminarPersona, name='eliminarPersona'),
]