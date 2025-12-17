from django.db import models

class HomePage(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    fraseInicio = models.CharField(max_length=255, blank=True, null=True)
    oqueeositeTit = models.CharField(max_length=1000, blank=True, null=True)
    oqueeosite = models.CharField(max_length=1000, blank=True, null=True)
    saibamaisTit =models.CharField(max_length=1000, blank=True, null=True)
    saibamais =models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Sobre(models.Model):
    paginaTitulo = models.TextField(max_length=200)
    sobre_nos = models.TextField()
    secaoTitulo = models.TextField(max_length=200)
    sobre_o_livro = models.TextField()
    galeria = models.ManyToManyField('Image', related_name='galerias')
    membros = models.ManyToManyField('Membro')

    def __str__(self):
        return "Página Sobre"

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Site(models.Model):
    titulo = models.CharField(max_length=50)
    contato = models.EmailField(max_length=254, null=True, blank=True)
    logo =models.ImageField(upload_to='logo/', null=True, blank=True)
    

class Image(models.Model):
    imagem = models.ImageField(upload_to='galeria_sobre/')

    def __str__(self):
        return f"Imagem {self.id}"

class Pagina(models.Model):
    numero_pagina = models.IntegerField()
    pagina= models.ImageField(upload_to='paginas_livro/')

    def __str__(self):
        return f"Página {self.numero_pagina}"
    
    class Meta:
        ordering = ['numero_pagina']


class Livro(models.Model):
    capa = models.ImageField(upload_to='administracao_page/',null=True, blank=True)
    pdf = models.FileField(upload_to='livro_pdf', null=True, blank=True)
    titulo = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField( null=True, blank=True)


class IdentidadeVisual(models.Model):
    cor_principal = models.CharField(max_length = 7, default ="#005EFF")
    cor_secundaria = models.CharField(max_length = 7, default ="#005EFF")
    cor_hover = models.CharField(max_length = 7, default ="#005EFF")
    



