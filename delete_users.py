import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from habits.models.usuario.model import Usuario
from habits.models.persona.model import Persona

# Borrar todos los usuarios
usuarios = Usuario.objects.all()
print(f"Borrando {usuarios.count()} registros de Usuario...")
usuarios.delete()

# Borrar todas las personas creadas por registro
personas = Persona.objects.all()
print(f"Borrando {personas.count()} registros de Persona...")
personas.delete()

# Borrar todos los usuarios de Django (excepto superuser)
usuarios_django = User.objects.exclude(is_superuser=True)
print(f"Borrando {usuarios_django.count()} usuarios de Django...")
usuarios_django.delete()

print("✓ Todos los usuarios han sido eliminados")
