from django.shortcuts import render, redirect
from .forms import CadastroForm
from livro3d.models import Livro, Pagina, Site
from livro3d.forms import LivroForm, PaginaForm, SiteForm

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


def administracao(request):
    return render(request, 'paineladmin.html')

def users(request):
    return render(request, 'users.html')

def paginas(request):
    paginas = Pagina.objects.all()

    return render(request, "paginas.html", {
        'paginas': paginas,
    })

def layout(request):
    return render(request, 'layout.html')

def configuracoes(request):
    site = Site.objects.first()
    siteForm = SiteForm(request.POST, request.FILES)
    
    if request.method == "POST":
        siteForm = SiteForm(request.POST, request.FILES)

        if siteForm.is_valid():
            siteForm.save()
            
            return redirect('configuracoes')

    else:
        siteForm = SiteForm()

    
    return render(request, 'configuracoes.html', {
        'siteForm': siteForm,
        'site': site,
    })

def livro_paginas(request):
    pagina_form = PaginaForm(request.POST, request.FILES)
    
    if request.method == "POST":
        pagina_form = PaginaForm(request.POST, request.FILES)

        if pagina_form.is_valid():
            pagina_form.save()

        return redirect('livro_paginas')

    else:
        pagina_form = PaginaForm()

    paginas = Pagina.objects.all()

    return render(request, "livro_paginas.html", {
        'pagina_form': pagina_form,
        'paginas': paginas,
    })

def gerenciar_livro(request):
    livro = Livro.objects.first()

    if request.method == "POST":
        livro_form = LivroForm(request.POST, request.FILES, instance=livro)
        pagina_form = PaginaForm(request.POST, request.FILES)

        if livro_form.is_valid():
            livro_form.save()

        if pagina_form.is_valid():
            pagina_form.save()

        return redirect('gerenciar_livro')

    else:
        livro_form = LivroForm(instance=livro)
        pagina_form = PaginaForm()

    paginas = Pagina.objects.all()

    return render(request, "livroform.html", {
    'livro_form': livro_form,
    'pagina_form': pagina_form,
    'paginas': paginas,
    'livro': livro,
})



def deletar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == "POST":
        livro.delete()
        return redirect('gerenciar_livro')

