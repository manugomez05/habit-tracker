from django.urls import path
from .views import persona, grupo, tareas
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
    path('tareas/', views.tareas, name='lista_tareas'),
    path('tareas/<int:id>/', views.verTarea, name='verTarea'),
    path('crear_tarea/', views.crearTarea, name='crearTarea'),
    path('modificar_tarea/<int:id>/', views.modificarTarea, name='modificarTarea'),
    path('eliminar_tarea/<int:id>/', views.eliminarTarea, name='eliminarTarea'),
]

