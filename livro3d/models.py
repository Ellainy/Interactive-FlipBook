from django.db import models

class HomePage(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    fraseInicio = models.CharField(max_length=255, blank=True, null=True)
    oqueeosite = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.titulo

class ModoLeitura(models.Model):
    MODOS_LEITURA = [
        ('flipbook', 'Flipbook'),
        ('pdf', 'PDF'),
    ]
    modo_leitura = models.CharField(max_length=10, choices=MODOS_LEITURA)
    sinopse = models.TextField()
    imagens = models.ImageField(upload_to='imagens_livro/')

    def __str__(self):
        return f"Livro: {self.id}"

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
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Image(models.Model):
    imagem = models.ImageField(upload_to='galeria_sobre/')

    def __str__(self):
        return f"Imagem {self.id}"

class Livro(models.Model):
    Titulo = models.ForeignKey(ModoLeitura, related_name='paginas', on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField( null=True, blank=True)
    imagem = models.ImageField(upload_to='paginas_livro/', null=True, blank=True)
    numero_pagina = models.IntegerField( null=True, blank=True)

    def __str__(self):
        return f"Página {self.numero_pagina} - {self.titulo}"
    
    class Meta:
        ordering = ['numero_pagina']
