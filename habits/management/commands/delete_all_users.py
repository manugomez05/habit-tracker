from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from habits.models.usuario.model import Usuario
from habits.models.persona.model import Persona

class Command(BaseCommand):
    help = 'Borra todos los usuarios excepto superusuarios'

    def handle(self, *args, **options):
        # Borrar registros de Usuario
        usuarios = Usuario.objects.all()
        count_usuarios = usuarios.count()
        usuarios.delete()
        self.stdout.write(self.style.SUCCESS(f'✓ {count_usuarios} registros de Usuario eliminados'))

        # Borrar registros de Persona
        personas = Persona.objects.all()
        count_personas = personas.count()
        personas.delete()
        self.stdout.write(self.style.SUCCESS(f'✓ {count_personas} registros de Persona eliminados'))

        # Borrar usuarios de Django (excepto superuser)
        usuarios_django = User.objects.exclude(is_superuser=True)
        count_django = usuarios_django.count()
        usuarios_django.delete()
        self.stdout.write(self.style.SUCCESS(f'✓ {count_django} usuarios de Django eliminados'))

        self.stdout.write(self.style.SUCCESS('✓ Todos los usuarios han sido eliminados'))
