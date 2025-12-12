from django.urls import path
from . import views

urlpatterns = [
    path('cadastre-se/', views.cadastro, name='cadastro'),
    path('administracao/', views.administracao, name='administracao'),
    path('gerenciar_livro/', views.gerenciar_livro, name='gerenciar_livro'),
    path('deletar_livro/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),
    path('livro_paginas/', views.livro_paginas, name='livro_paginas'),
    path('users/', views.users, name='users'),
    path('paginas/', views.paginas, name='paginas'),
    path('layout/', views.layout, name='layout'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
]