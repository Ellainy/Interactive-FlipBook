from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    
    context = {'form': form}
    return render(request, 'registration/cadastro.html', context)

def sair(request):
    logout(request)
    return redirect('index')