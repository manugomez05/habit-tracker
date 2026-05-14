from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habitos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=8)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)

    miembros = models.ManyToManyField(Persona)

    def __str__(self):
        return self.nombre