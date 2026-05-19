from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.IntegerField(max_length=8)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}" 
class Grupo(models.Model):
    nombre = models.CharField(max_length=100)

    miembros = models.ManyToManyField(Persona)

    def __str__(self):
        return self.nombre
class Habitos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo
