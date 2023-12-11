from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import PQRS


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña2', widget=forms.PasswordInput)
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'groups']
        help_texts = {k: "" for k in fields}

from .models import PQRS

class PQRSForm(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ['case', 'description', 'user', 'answer']