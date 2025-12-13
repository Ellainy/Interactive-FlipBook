from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import HomePage, Livro, Sobre, Pagina
from .forms import LivroForm, HomePageForm, SobreForm, PaginaForm, CadastroForm

def index(request):
    home_page = HomePage.objects.first() 
    sobre = Sobre.objects.prefetch_related('galeria').first()
    imagens_galeria = sobre.galeria.all() if sobre else []
    livro = Livro.objects.first() 

    return render(request, 'index.html', {
        'home_page': home_page,
        'sobre': sobre,
        'imagens_galeria': imagens_galeria,
        'livro': livro
    })

def livro(request):
    livro = Livro.objects.first() 
    return render(request, 'livro.html', {
        'livro': livro,
    })

def lerlivro(request):
    livro = Livro.objects.first() 
    pagina = Pagina.objects.all().order_by('numero_pagina')
    return render(request, 'lerlivro.html', {
        'paginas': pagina,
        'livro': livro  
        })

def sobre(request):
    sobre_info = Sobre.objects.prefetch_related('galeria', 'membros').first()
    livro = Livro.objects.first()
    return render(request, 'sobre.html', {
        'sobre': sobre_info,
        'livro': livro
    })

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

@login_required
def administracao(request):
    return render(request, 'paineladmin.html')

@login_required
def editar_textos(request):
    home = HomePage.objects.first()
    sobre = Sobre.objects.first()

    if request.method == "POST":
        if "salvar_home" in request.POST:  
            home_form = HomePageForm(request.POST, instance=home)
            sobre_form = SobreForm(instance=sobre) 
            if home_form.is_valid():
                home_form.save()
                return redirect('editar_textos')

        elif "salvar_sobre" in request.POST:  
            sobre_form = SobreForm(request.POST, instance=sobre)
            home_form = HomePageForm(instance=home)
            if sobre_form.is_valid():
                sobre_form.save()
                return redirect('editar_textos')

    else:
        home_form = HomePageForm(instance=home)
        sobre_form = SobreForm(instance=sobre)

    return render(request, "site.html", {
        "home_form": home_form,
        "sobre_form": sobre_form,
    })