from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório.')

    class Meta:
        model = User
        fields = ['username', 'email']