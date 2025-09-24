from .models import User
from django.contrib.auth.forms import BaseUserCreationForm

class CadastroForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']