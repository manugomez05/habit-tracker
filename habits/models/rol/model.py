from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
    
    def __str__(self):
        return self.nombre