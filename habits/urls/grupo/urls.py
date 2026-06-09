from django.urls import path
from ...views.grupo.views import grupo, verGrupo, modificarGrupo, crearGrupo, eliminarGrupo

urlpatterns = [
    path('grupos/', grupo, name='lista_grupos'),
    path('grupos/<int:id>/', verGrupo, name='verGrupo'),
    path('modificar_grupo/<int:id>/', modificarGrupo, name='modificarGrupo'),
    path('crear_grupo/', crearGrupo, name='crearGrupo'),
    path('eliminar_grupo/<int:id>/', eliminarGrupo, name='eliminarGrupo'),
]
