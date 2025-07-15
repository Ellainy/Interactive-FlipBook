from django.shortcuts import render
from .models import HomePage, Livro, Sobre, ModoLeitura

def index(request):
    home_page = HomePage.objects.first() 
    sobre = Sobre.objects.prefetch_related('galeria').first()
    imagens_galeria = sobre.galeria.all() if sobre else []

    return render(request, 'index.html', {
        'home_page': home_page,
        'sobre': sobre,
        'imagens_galeria': imagens_galeria
    })

def livro(request):
    livro = Livro.objects.first()
    #paginas = livro.paginas.all()  
    return render(request, 'livro.html', {'livro': livro})

def sobre(request):
    sobre_info = Sobre.objects.prefetch_related('galeria', 'membros').first()
    return render(request, 'sobre.html', {'sobre': sobre_info})

def lerlivro(request):
    return render(request, 'lerlivro.html')


