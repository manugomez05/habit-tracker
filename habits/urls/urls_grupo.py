from .views.views_grupo import grupo, verGrupo, modificarGrupo, crearGrupo, eliminarGrupo
from . import views
from django.urls import path

urlpatterns = [
path('grupos/',grupo, name='lista_grupos'),
    path('grupos/<int:id>/', views.views_grupo.verGrupo, name='verGrupo'),
    path('modificar_grupo/<int:id>/', views.views_grupo.modificarGrupo, name='modificarGrupo'),
    path('crear_grupo/', views.views_grupo.crearGrupo, name='crearGrupo'),
    path('eliminar_grupo/<int:id>/', views.views_grupo.eliminarGrupo, name='eliminarGrupo'),
]