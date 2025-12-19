from django import forms
from .models import Livro, Index, Sobre, Pagina, Site, IdentidadeVisual

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

class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['titulo', 'frase_inicio', 'o_que_e_site_titulo', 'o_que_e_o_site']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'frase_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'o_que_e_site_titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'o_que_e_o_site': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
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
        fields = ['titulo', 'contato', 'logo', 'saiba_mais_footer']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contato': forms.EmailInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'saiba_mais_footer': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class IdentidadeVisualForm(forms.ModelForm):
    class Meta:
        model = IdentidadeVisual
        fields = "__all__"

    cor_principal = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "class":"form-control form-control-color"}))
    cor_secundaria = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "class":"form-control form-control-color"}))
    cor_hover = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "class":"form-control form-control-color"}))
