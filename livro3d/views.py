from django.shortcuts import render
from .models import HomePage, Livro, Sobre, Pagina

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
        'livro': livro    
    })

def lerlivro(request):
    pagina = Pagina.objects.all().order_by('numero_pagina')
    return render(request, 'lerlivro.html', {
        'paginas': pagina
        })


def sobre(request):
    sobre_info = Sobre.objects.prefetch_related('galeria', 'membros').first()
    livro = Livro.objects.first()
    return render(request, 'sobre.html', {
        'sobre': sobre_info,
        'livro': livro
    })




