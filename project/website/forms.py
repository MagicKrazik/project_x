from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from .models import Appointment

class RegistrationForm(UserCreationForm):
    usable_password = None
    email = forms.EmailField(
        required=True,
        label=_("Correo electrónico"),
        error_messages={
            'unique': _("Ya existe un usuario con este correo electrónico."),
        }
    )
    phone_number = forms.CharField(
        max_length=10,
        min_length=10, 
        required=False,
        label=_("Número de teléfono")
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        labels = {
            'username': _('Nombre de usuario'),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = _("Nombre de usuario")
        self.fields['password1'].label = _("Contraseña")
        self.fields['password2'].label = _("Confirmar contraseña")
        
        # You can customize the help text if needed
        # self.fields['username'].help_text = _("Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ solamente.")
        # self.fields['password1'].help_text = _("Tu contraseña debe contener al menos 8 caracteres.")
        # self.fields['password2'].help_text = _("Ingresa la misma contraseña que antes, para verificación.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user
    

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'meeting_type', 'location', 'additional_message', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'] = forms.ModelChoiceField(
                queryset=CustomUser.objects.filter(pk=user.pk),
                initial=user,
                widget=forms.HiddenInput()
            )    