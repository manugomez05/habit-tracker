from django.urls import path
from ...views.tarea.views import tareas, verTarea, modificarTarea, crearTarea, eliminarTarea, completarTarea

urlpatterns = [
    path('tareas/', tareas, name='lista_tareas'),
    path('tareas/<int:id>/', verTarea, name='verTarea'),
    path('modificar_tarea/<int:id>/', modificarTarea, name='modificarTarea'),
    path('crear_tarea/', crearTarea, name='crearTarea'),
    path('eliminar_tarea/<int:id>/', eliminarTarea, name='eliminarTarea'),
    path('completar_tarea/<int:id>/', completarTarea, name='completarTarea'),
]
