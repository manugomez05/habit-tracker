from django.db import models
from django.contrib.auth.models import User
from habits.models.persona.model import Persona

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='usuario')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'.strip() or self.user.username
