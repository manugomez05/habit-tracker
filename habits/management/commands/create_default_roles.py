from django.core.management.base import BaseCommand
from habits.models.rol.model import Rol

class Command(BaseCommand):
    help = 'Crea roles por defecto'

    def handle(self, *args, **options):
        roles_default = ['Administrador', 'Lider', 'Integrante']
        
        for rol_nombre in roles_default:
            rol, created = Rol.objects.get_or_create(nombre=rol_nombre)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Rol "{rol_nombre}" creado'))
            else:
                self.stdout.write(f'- Rol "{rol_nombre}" ya existe')
        
        self.stdout.write(self.style.SUCCESS('✓ Roles configurados'))
