from django.urls import path
from . import views

urlpatterns = [
    # Rotas Públicas
    path('', views.index, name='index'),
    path('livro/', views.livro, name='livro'),
    path('sobre/', views.sobre, name='sobre'),
    path('lerlivro/', views.lerlivro, name='lerlivro'),
    path('layout/', views.layout, name='layout'),

    # Rotas Administrativas
    path('administracao/', views.administracao, name='administracao'),
    path('editar-textos/', views.editar_textos, name='editar_textos'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('indexform/', views.indexform, name='indexform'),
    path('sobreform/', views.sobreform, name='sobreform'),
    path('gerenciar_livro/', views.gerenciar_livro, name='gerenciar_livro'),
    path('livro_paginas/', views.livro_paginas, name='livro_paginas'),
    path('paginas/', views.paginas, name='paginas'),
    path('deletar_livro/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),
]