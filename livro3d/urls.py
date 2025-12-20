from django.urls import path
from . import views

urlpatterns = [
    # Páginas Públicas
    path('', views.index, name='index'),
    path('livro/', views.livro, name='livro'),
    path('sobre/', views.sobre, name='sobre'),
    path('lerlivro/', views.lerlivro, name='lerlivro'),

    # Painéis e Configurações
    path('administracao/', views.administracao, name='administracao'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('layout/', views.layout, name='layout'),

    # Edição de Conteúdo
    path('editar-textos/', views.editar_textos, name='editar_textos'), # Corrige o erro "Reverse not found"
    
    # Formulários
    path('indexform/', views.indexform, name='indexform'),
    path('sobreform/', views.sobreform, name='sobreform'),
    path('livroform/', views.livroform, name='livroform'),

    # Gestão do Livro
    path('gerenciar_livro/', views.gerenciar_livro, name='gerenciar_livro'),
    path('livro_paginas/', views.livro_paginas, name='livro_paginas'),
    path('paginas/', views.paginas, name='paginas'),
    path('deletar_livro/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),
    
    # Gestão da Galeria (Carrossel)
    path('gerenciar-galeria/', views.imageform, name='imageform'),
    path('galeria/excluir/<int:foto_id>/', views.excluir_foto, name='excluir_foto'),
]