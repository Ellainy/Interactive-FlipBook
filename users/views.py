from django.shortcuts import render, redirect
from .forms import CadastroForm


def cadastro(request):
    form = CadastroForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = CadastroForm()
        context = {
            'form': form
        }
        return render(request, 'registration/cadastro.html', context)


def profile(request):
    return render(request, 'perfil.html')

def editar(request):
    return render(request, 'editprofile.html')

def administracao(request):
    return render(request, 'paineladmin.html')