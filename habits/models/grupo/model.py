from django.db import models
from django.contrib.auth.models import User
from ..persona.model import Persona

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    miembros = models.ManyToManyField(Persona)

    def __str__(self):
        return self.nombre
