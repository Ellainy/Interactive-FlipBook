from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Pega o modelo de usuário correto (seja o padrão ou personalizado)
User = get_user_model()

class CadastroForm(UserCreationForm):
    # Tornando o email obrigatório
    email = forms.EmailField(required=True, help_text='Obrigatório.')

    class Meta:
        model = User
        # IMPORTANTE: Nunca coloque 'password' aqui. O UserCreationForm já cuida disso.
        fields = ['username', 'email']