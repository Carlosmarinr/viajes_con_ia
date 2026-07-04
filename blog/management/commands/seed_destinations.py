from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Destination


class Command(BaseCommand):
    help = 'Seed the blog with a few sample Venezuelan destinations'

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(username='admin', defaults={'is_staff': True, 'is_superuser': True})
        if user.password == '':
            user.set_password('admin123')
            user.save()

        destinations = [
            {
                'title': 'Margarita',
                'summary': 'Playas paradisíacas y un ambiente lleno de vida.',
                'description': 'Isla Margarita combina playas de ensueño con gastronomía y cultura.',
                'location': 'Nueva Esparta',
                'featured': True,
            },
            {
                'title': 'Mérida',
                'summary': 'Montañas, aventura y los mejores paisajes andinos.',
                'description': 'Mérida ofrece rutas, parques nacionales y una temperatura fresca todo el año.',
                'location': 'Mérida',
                'featured': True,
            },
            {
                'title': 'Canaima',
                'summary': 'Salto Ángel y selva virgen en el corazón de Venezuela.',
                'description': 'Canaima es uno de los destinos más emblemáticos del país por sus formaciones rocosas y naturaleza.',
                'location': 'Bolívar',
                'featured': True,
            },
        ]

        for data in destinations:
            Destination.objects.get_or_create(
                title=data['title'],
                defaults={
                    'summary': data['summary'],
                    'description': data['description'],
                    'location': data['location'],
                    'featured': data['featured'],
                    'author': user,
                },
            )

        self.stdout.write(self.style.SUCCESS('Sample destinations created successfully.'))
