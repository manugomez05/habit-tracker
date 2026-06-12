from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.IntegerField()
    rol = models.ForeignKey('habits.Rol', on_delete=models.SET_NULL, null=True, blank=True, related_name='personas')

    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
