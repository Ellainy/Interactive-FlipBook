from django.shortcuts import render, redirect, get_object_or_404
from .models import HomePage, Livro, Sobre, Pagina, ModoLeitura
from .forms import LivroForm, HomePageForm, SobreForm, PaginaForm, ModoLeituraForm

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
    modoLeitura = ModoLeitura.objects.first()
    return render(request, 'livro.html', {
        'livro': livro,
        'modoLeitura': modoLeitura,  
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

def gerenciar_livro(request):
    livro = Livro.objects.first()
    modo = ModoLeitura.objects.first()

    if request.method == "POST":
        livro_form = LivroForm(request.POST, request.FILES, instance=livro)
        pagina_form = PaginaForm(request.POST, request.FILES)
        modo_form = ModoLeituraForm(request.POST, request.FILES, instance=modo)

        if livro_form.is_valid() and modo_form.is_valid():
            livro_form.save()
            modo_form.save()

        if pagina_form.is_valid():
            pagina_form.save()

        return redirect('gerenciar_livro')

    else:
        livro_form = LivroForm(instance=livro)
        pagina_form = PaginaForm()
        modo_form = ModoLeituraForm(instance=modo)

    paginas = Pagina.objects.all()

    return render(request, "livroform.html", {
        'livro_form': livro_form,
        'pagina_form': pagina_form,
        'modo_form': modo_form,
        'paginas': paginas,
    })


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
