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
    sobre_nos = models.TextField()
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
    imgs = models.ImageField(upload_to='galeria_sobre/', null=True, blank=True)
    titulo = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField( null=True, blank=True)
