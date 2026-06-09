from django.urls import path
from .views_base import api_personas
from . import views_base

urlpatterns = [
    path('', views_base.home, name='home'),
    path('api/personas/', api_personas, name='api_personas'),
    path('api/grupos/', views_base.api_grupo, name='api_grupos'),
    path('api/grupos/crear/', views_base.api_crear_grupo, name='api_crear_grupo'),
    path('api/grupos/<int:id>/', views_base.api_modificar_grupo, name='api_modificar_grupo'),
    path('api/grupos/<int:id>/eliminar/', views_base.api_eliminar_grupo, name='api_eliminar_grupo'),
    path('api/tareas/', views_base.api_tareas, name='api_tareas'),
    path('api/tareas/<int:id>/', views_base.api_tarea_detail, name='api_tarea_detail'),
    path('clima/', views_base.clima, name='clima'),
] 
  
