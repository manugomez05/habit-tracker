from django.db import models
from django.contrib.auth.models import User
from ..persona.model import Persona

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    personas = models.ManyToManyField(Persona, related_name='tareas')

    def __str__(self):
        return self.titulo

