from django.db import models
from django.contrib.auth.models import User

from .models_grupo import Grupo



class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo
