# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('nombre', 'username', 'email', 'telefono', 'password1', 'password2', 'metodo_pago')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre completo"
        self.fields['username'].label = "Nombre de usuario"
        self.fields['email'].label = "Correo electrónico"
        self.fields['telefono'].label = "Teléfono"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['metodo_pago'].label = "Método de pago"

        # Remove all help texts and widgets
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs = {}
