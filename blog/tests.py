from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Destination


class DestinationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='tester', password='StrongPass123')

    def test_destination_slug_is_generated(self):
        destination = Destination.objects.create(
            title='Canaima',
            summary='Una maravilla',
            description='Un destino espectacular',
            location='Bolívar',
            author=self.user,
        )
        self.assertEqual(destination.slug, 'canaima')

    def test_home_page_displays_destinations(self):
        Destination.objects.create(
            title='Mérida',
            summary='Montañas y aventura',
            description='Un lugar ideal para viajar',
            location='Mérida',
            author=self.user,
        )
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mérida')
