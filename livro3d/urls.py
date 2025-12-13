from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/', views.livro, name='livro'),
    path('sobre/', views.sobre, name='sobre'),
    path('lerlivro/', views.lerlivro, name='lerlivro'),
    path('cadastre-se/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.sair, name='logout'),
    path('administracao/', views.administracao, name='administracao'),
    path('editar-textos/', views.editar_textos, name='editar_textos'),
]