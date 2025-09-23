from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/', views.livro, name='livro'),
    path('sobre/', views.sobre, name='sobre'),
    path('lerlivro/', views.lerlivro, name='lerlivro'),
    path('gerenciar-livro/', views.gerenciar_livro, name='gerenciar_livro'),
    path('deletar_livro/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),
    path('editar-textos/', views.editar_textos, name='editar_textos'),

]