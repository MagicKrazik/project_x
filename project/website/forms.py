from django import forms
from django.core.validators import MinValueValidator

class RegistrationForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    usuario = forms.CharField(max_length=50, label='Usuario')
    telefono = forms.CharField(max_length=15, label='Teléfono')
    correo = forms.EmailField(label='Correo electrónico')
    edad = forms.IntegerField(validators=[MinValueValidator(18)], label='Edad')
    PAISES_CHOICES = [
        ('', 'Selecciona un país'),
        ('es', 'España'),
        ('mx', 'México'),
        ('ar', 'Argentina'),
        ('co', 'Colombia'),
        ('pe', 'Perú'),
        # Add more countries as needed
    ]
    pais = forms.ChoiceField(choices=PAISES_CHOICES, label='País')