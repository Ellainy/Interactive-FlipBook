from django.urls import path
from . import views

urlpatterns = [
    path('cadastre-se/', views.cadastro, name='cadastro'),
    path('perfil/', views.profile, name='perfil'),
    path('editarPerfil/', views.editar, name='editarPerfil'),
    path('administracao/', views.administracao, name='administracao'),
    path('users/', views.users, name='users'),
    path('paginas/', views.paginas, name='paginas'),
    path('layout/', views.layout, name='layout'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
]