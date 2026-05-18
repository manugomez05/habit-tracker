from django.urls import path
from .views import persona, grupo
from . import views

urlpatterns = [
    path('',persona),
    path('personas/',persona, name='lista_personas'),
    path('personas/<int:id>/', views.verPersona, name='verPersona'),
    path('modificar_persona/<int:id>/', views.modificarPersona, name='modificarPersona'),
    path('crear_persona/', views.crearPersona, name='crearPersona'),
    path('eliminar_persona/<int:id>/', views.eliminarPersona, name='eliminarPersona'),
    path('grupos/', views.grupo, name='lista_grupos'),
    path('grupos/<int:id>/', views.verGrupo, name='verGrupo'),
    path('crear_grupo/', views.crearGrupo, name='crearGrupo'),
    path('modificar_grupo/<int:id>/', views.modificarGrupo, name='modificarGrupo'),
    path('eliminar_grupo/<int:id>/', views.eliminarGrupo, name='eliminarGrupo'),
]

