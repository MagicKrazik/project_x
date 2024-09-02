# tests.py
from django.test import TestCase
from django.urls import reverse
from .models import User

class RegistrationTestCase(TestCase):
    def test_registration_form_display(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Regístrate Aquí')

    def test_registration_success(self):
        data = {
            'nombre': 'Juan Pérez',
            'username': 'juanperez',
            'email': 'juan@example.com',
            'telefono': '1234567890',
            'password1': 'MyStr0ngP@ssw0rd!',
            'password2': 'MyStr0ngP@ssw0rd!',
            'metodo_pago': 'online'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful registration
        self.assertTrue(User.objects.filter(username='juanperez').exists())

    def test_registration_weak_password(self):
        data = {
            'nombre': 'Juan Pérez',
            'username': 'juanperez',
            'email': 'juan@example.com',
            'telefono': '1234567890',
            'password1': 'weak',
            'password2': 'weak',
            'metodo_pago': 'online'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # Expecting the form to be re-displayed
        self.assertContains(response, 'Esta contraseña es demasiado corta')

    # Add more test methods for other scenarios