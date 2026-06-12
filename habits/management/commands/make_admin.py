from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from habits.models.usuario.model import Usuario
from habits.models.persona.model import Persona
from habits.models.rol.model import Rol

class Command(BaseCommand):
    help = 'Convierte un usuario en administrador'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username del usuario a convertir en admin')

    def handle(self, *args, **options):
        username = options['username']
        
        try:
            user = User.objects.get(username=username)
            persona = user.perfil.persona
            rol_admin = Rol.objects.get(nombre='Administrador')
            
            persona.rol = rol_admin
            persona.save()
            
            self.stdout.write(self.style.SUCCESS(f'✓ Usuario "{username}" es ahora Administrador'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'✗ Usuario "{username}" no existe'))
        except:
            self.stdout.write(self.style.ERROR('✗ Error al convertir el usuario en administrador'))
