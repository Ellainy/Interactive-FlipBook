from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Index, Livro, Sobre, Pagina, Site, IdentidadeVisual, ModoLeitura, Image, Membro
from .forms import LivroForm, IndexForm, SobreForm, PaginaForm, SiteForm, IdentidadeVisualForm, ImageForm, MembroForm

def index(request):
    index = Index.objects.first()
    galeria = Image.objects.all()
    return render(request, 'index.html', {
        'index': index,
        'galeria': galeria,
    })

def livro(request):
    livro = Livro.objects.first() 
    modoleitura = ModoLeitura.objects.first() 
    galeria = Image.objects.all() 

    return render(request, 'livro.html', {
        'livro': livro,
        'modoLeitura' : modoleitura,
        'galeria' : galeria,
    })

def lerlivro(request):
    livro = Livro.objects.first() 
    pagina = Pagina.objects.all().order_by('numero_pagina')
    return render(request, 'lerlivro.html', {
        'paginas': pagina,
        'livro': livro  
    })

def sobre(request):
    sobre_info = Sobre.objects.first()
    livro = Livro.objects.first()
    membros = Membro.objects.all

    return render(request, 'sobre.html', {
        'sobre': sobre_info,
        'livro': livro,
        "membros": membros
    })

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
    livro = Livro.objects.first()
    livro_id = livro.id if livro else None
    return render(request, 'paineladmin.html', {'livro_id': livro_id})

@login_required
def configuracoes(request):
    site = Site.objects.first()
    
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
def indexform(request):
    home = Index.objects.first()
    
    if request.method == "POST":
        home_form = IndexForm(request.POST, request.FILES, instance=home)
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
    membros = Membro.objects.all()

    sobre_form = SobreForm(instance=sobre)
    membro_form = MembroForm()

    if request.method == "POST":
        if 'salvar_sobre' in request.POST:
            sobre_form = SobreForm(request.POST, request.FILES, instance=sobre)
            if sobre_form.is_valid():
                sobre_form.save()
                return redirect('sobreform')

        elif 'salvar_membro' in request.POST:
            membro_id = request.POST.get('membro_id')
            if membro_id:
                membro = get_object_or_404(Membro, id=membro_id)
                membro_form = MembroForm(request.POST, request.FILES, instance=membro)
            else:
                membro_form = MembroForm(request.POST, request.FILES)
            
            if membro_form.is_valid():
                membro_form.save()
                return redirect('sobreform')

    return render(request, "sobreform.html", {
        "sobre_form": sobre_form,
        "membro_form": membro_form,
        "membros": membros
    })

@login_required
def excluir_membro(request, id):
    membro = get_object_or_404(Membro, id=id)
    if request.method == "POST":
        membro.delete()
        return redirect('sobreform')
    return redirect('sobreform')

@login_required
def livroform(request):
    livro = Livro.objects.first()

    if request.method == "POST":
        livro_form = LivroForm(request.POST, request.FILES, instance=livro)
        if livro_form.is_valid():
            livro_form.save()
            return redirect('livroform')
    else:
        livro_form = LivroForm(instance=livro)

    return render(request, "livroform.html", {
        "livro_form": livro_form
    })

@login_required
def livro_paginas(request):
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

@login_required
def excluir_pagina(request, id):
    pagina = get_object_or_404(Pagina, id=id)

    if request.method == "POST":
        pagina.delete()
        return redirect('paginas')

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
def imageform(request):
    if request.method == "POST":
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            return redirect('imageform')
    else:
        image_form = ImageForm()

    imagens = Image.objects.all()

    return render(request, "galeriaForm.html", {
        "form": image_form,
        "imagens": imagens
    })

@login_required
def excluir_foto(request, foto_id):
    foto = get_object_or_404(Image, id=foto_id)
    foto.delete()
    return redirect('imageform')

@login_required
def deletar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()
    return redirect('administracao')

@login_required
def editar_textos(request):
    return render(request, 'editar_textos.html')