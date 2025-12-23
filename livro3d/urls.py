from django.urls import path
from . import views

urlpatterns = [
    # Páginas do Site
    path('', views.index, name='index'),
    path('livro/', views.livro, name='livro'),
    path('ler-livro/', views.lerlivro, name='lerlivro'),
    path('sobre/', views.sobre, name='sobre'),
    path('layout/', views.layout, name='layout'),

    # Formulários / Admin
    path('administracao/', views.administracao, name='administracao'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    
    # Edição de Textos e Conteúdo
    path('editar-home/', views.indexform, name='indexform'),
    path('editar-sobre/', views.sobreform, name='sobreform'),
    path('excluir-membro/<int:id>/', views.excluir_membro, name='excluir_membro'),
    path('editar-livro/', views.livroform, name='livroform'),
    path('editar-textos/', views.editar_textos, name='editar_textos'),

    # Gerenciamento de Páginas e Livro
    path('gerenciar-paginas/', views.livro_paginas, name='livro_paginas'),
    path('gerenciar-livro-completo/', views.gerenciar_livro, name='gerenciar_livro'),
    path('paginas/', views.paginas, name='paginas'),
    path('deletar-livro/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),
    
    # Galeria
    path('galeria/', views.imageform, name='imageform'),
    path('galeria/excluir/<int:foto_id>/', views.excluir_foto, name='excluir_foto'),
]