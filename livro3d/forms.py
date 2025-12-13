from django import forms
from django.contrib.auth import get_user_model # <--- Importação necessária
from django.contrib.auth.forms import UserCreationForm
from .models import Livro, HomePage, Sobre, Pagina, Site

# Isso pega o seu modelo 'users.User' automaticamente
User = get_user_model()

# --- FORMULÁRIO DE CADASTRO ---
class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório.')

    class Meta:
        model = User # Agora aponta para o modelo correto
        fields = ['username', 'email']

# --- DEMAIS FORMULÁRIOS ---

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['capa', 'titulo', 'pdf', 'descricao']  
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título do livro'}),
            'capa': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escreva a descrição'}),
            'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['numero_pagina', 'pagina']
        widgets = {
            'numero_pagina': forms.NumberInput(attrs={'class': 'form-control'}),
            'pagina': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = ['titulo', 'fraseInicio', 'oqueeositeTit', 'oqueeosite', 'saibamaisTit', 'saibamais']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fraseInicio': forms.TextInput(attrs={'class': 'form-control'}),
            'oqueeositeTit': forms.TextInput(attrs={'class': 'form-control'}),
            'oqueeosite': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'saibamaisTit': forms.TextInput(attrs={'class': 'form-control'}),
            'saibamais': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SobreForm(forms.ModelForm):
    class Meta:
        model = Sobre
        fields = ['paginaTitulo', 'sobre_nos', 'secaoTitulo', 'sobre_o_livro']
        widgets = {
            'paginaTitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sobre_nos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'secaoTitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sobre_o_livro': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['titulo', 'contato', 'logo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contato': forms.EmailInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }