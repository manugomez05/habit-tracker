from django.db import models
from django.contrib.auth.models import User
from ..persona.model import Persona

class Tarea(models.Model):
    DIFICULTAD_BAJA = 'Baja'
    DIFICULTAD_MEDIA = 'Media'
    DIFICULTAD_ALTA = 'Alta'
    DIFICULTAD_CHOICES = [
        (DIFICULTAD_BAJA, 'Baja'),
        (DIFICULTAD_MEDIA, 'Media'),
        (DIFICULTAD_ALTA, 'Alta'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES, default=DIFICULTAD_BAJA)
    completada = models.BooleanField(default=False)
    personas = models.ManyToManyField(Persona, related_name='tareas')

    def __str__(self):
        return self.titulo

