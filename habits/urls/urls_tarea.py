from .views.views_tarea import tareas, verTarea, modificarTarea, crearTarea, eliminarTarea
from . import views
from django.urls import path

urlpatterns = [
path('tareas/',tareas, name='lista_tareas'),
    path('tareas/<int:id>/', views.views_tarea.verTarea, name='verTarea'),
    path('modificar_tarea/<int:id>/', views.views_tarea.modificarTarea, name='modificarTarea'),
    path('crear_tarea/', views.views_tarea.crearTarea, name='crearTarea'),
    path('eliminar_tarea/<int:id>/', views.views_tarea.eliminarTarea, name='eliminarTarea'),
]