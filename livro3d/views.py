from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import HomePage, Livro, Sobre, Pagina, Site
from .forms import LivroForm, HomePageForm, SobreForm, PaginaForm, SiteForm

# --- VIEWS PÚBLICAS ---

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

def layout(request):
    return render(request, 'layout.html')


# --- VIEWS ADMINISTRATIVAS (PROTEGIDAS) ---

@login_required
def administracao(request):
    return render(request, 'paineladmin.html')

@login_required
def configuracoes(request):
    site = Site.objects.first()
    siteForm = SiteForm(request.POST, request.FILES) if request.method == "POST" else SiteForm(instance=site) # Correção aqui para preencher o form se existir
    
    if request.method == "POST":
        siteForm = SiteForm(request.POST, request.FILES, instance=site) # Correção: passar a instance para editar, não criar novo
        if siteForm.is_valid():
            siteForm.save()
            return redirect('configuracoes')
    else:
        siteForm = SiteForm(instance=site) # Preenche com dados existentes

    return render(request, 'configuracoes.html', {
        'siteForm': siteForm,
        'site': site,
    })

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
        
        # Nota: Normalmente não salvamos pagina aqui se for apenas editar o livro, 
        # mas mantive sua lógica original se o form vier preenchido
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
    return redirect('gerenciar_livro') # Caso não seja POST