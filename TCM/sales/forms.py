
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sales
from. models import Services

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña2', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['name', 'user', 'amount', 'date', 'service']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza las opciones del campo de servicio
        self.fields['service'].queryset = Services.objects.all()