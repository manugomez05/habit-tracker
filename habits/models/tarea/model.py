from django.db import models
from django.contrib.auth.models import User
from ..persona.model import Persona

class Tarea(models.Model):
    DIFICULTAD_BAJA = '1'
    DIFICULTAD_MEDIA = '2'
    DIFICULTAD_ALTA = '3'
    DIFICULTAD_CHOICES = [
        (DIFICULTAD_BAJA, '1 - Baja'),
        (DIFICULTAD_MEDIA, '2 - Media'),
        (DIFICULTAD_ALTA, '3 - Alta'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    dificultad = models.CharField(max_length=1, choices=DIFICULTAD_CHOICES, default=DIFICULTAD_BAJA)
    completada = models.BooleanField(default=False)
    google_calendar_event_id = models.CharField(max_length=255, blank=True, null=True)
    google_calendar_sync_error = models.TextField(blank=True)
    personas = models.ManyToManyField(Persona, related_name='tareas')

    def __str__(self):
        return self.titulo

