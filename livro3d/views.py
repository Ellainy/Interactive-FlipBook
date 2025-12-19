from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Index, Livro, Sobre, Pagina, Site, IdentidadeVisual
from .forms import LivroForm, IndexForm, SobreForm, PaginaForm, SiteForm, IdentidadeVisualForm

# VIEWS PÚBLICAS 

def index(request):
    index = Index.objects.first() 
    sobre = Sobre.objects.prefetch_related('galeria').first()
    imagens_galeria = sobre.galeria.all() if sobre else []
    livro = Livro.objects.first() 

    return render(request, 'index.html', {
        'index': index,
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



# VIEWS ADMINISTRATIVAS
def layout(request):
    identidade = IdentidadeVisual.objects.first()

    if request.method == "POST":
        form = IdentidadeVisualForm(
            request.POST,
            request.FILES,
            instance=identidade
        )
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IdentidadeVisualForm(instance=identidade)

    return render(request, 'layout.html', {
        'form': form,
    })


@login_required
def administracao(request):
    return render(request, 'paineladmin.html')

@login_required
def configuracoes(request):
    site = Site.objects.first()
    siteForm = SiteForm(request.POST, request.FILES) if request.method == "POST" else SiteForm(instance=site) 
    
    if request.method == "POST":
        siteForm = SiteForm(request.POST, request.FILES, instance=site)
        if siteForm.is_valid():
            siteForm.save()
            return redirect('configuracoes')
    else:
        siteForm = SiteForm(instance=site) 

    return render(request, 'configuracoes.html', {
        'siteForm': siteForm,
        'site': site,
    })

@login_required
def editar_textos(request):
    home = Index.objects.first()
    sobre = Sobre.objects.first()

    if request.method == "POST":
        if "salvar_home" in request.POST:  
            home_form = IndexForm(request.POST, instance=home)
            sobre_form = SobreForm(instance=sobre) 
            if home_form.is_valid():
                home_form.save()
                return redirect('editar_textos')

        elif "salvar_sobre" in request.POST:  
            sobre_form = SobreForm(request.POST, instance=sobre)
            home_form = IndexForm(instance=home)
            if sobre_form.is_valid():
                sobre_form.save()
                return redirect('editar_textos')
    else:
        home_form = IndexForm(instance=home)
        sobre_form = SobreForm(instance=sobre)

    return render(request, "site.html", {
        "home_form": home_form,
        "sobre_form": sobre_form,
    })

@login_required
def indexform(request):
    home = Index.objects.first()
    home_form = IndexForm(request.POST, request.FILES) if request.method == "POST" else IndexForm(instance=home) 
    

    if request.method == "POST":
        if home_form.is_valid():
            home_form.save()
            return redirect('indexform')

    else:
        home_form = IndexForm(instance=home)

    return render(request, "indexform.html", {
        "home_form": home_form
    })

@login_required
def sobreform(request):
    sobre = Sobre.objects.first()
    sobre_form = SobreForm(request.POST, request.FILES) if request.method == "POST" else SobreForm(instance=sobre) 
    

    if request.method == "POST":
        if sobre_form.is_valid():
            sobre_form.save()
            return redirect('sobreform')

    else:
        sobre_form = SobreForm(instance=sobre)

    return render(request, "sobreform.html", {
        "sobre_form": sobre_form
    })


@login_required
def livro_paginas(request):
    pagina_form = PaginaForm(request.POST, request.FILES) if request.method == "POST" else PaginaForm()
    
    if request.method == "POST":
        if pagina_form.is_valid():
            pagina_form.save()
            return redirect('livro_paginas')

    paginas = Pagina.objects.all()
    return render(request, "livro_paginas.html", {
        'pagina_form': pagina_form,
        'paginas': paginas,
    })

@login_required
def paginas(request):
    paginas = Pagina.objects.all()
    return render(request, "paginas.html", {
        'paginas': paginas,
    })

@login_required
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

@login_required
def deletar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == "POST":
        livro.delete()
        return redirect('gerenciar_livro')
    return redirect('gerenciar_livro') 
    
