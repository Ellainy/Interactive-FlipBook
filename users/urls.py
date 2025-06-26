from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path("perfil/", views.verperfil, name = "verperfil"),
    path("editar_perfil/", views.editarperfil, name = "editarperfil"),
    path("painel/", views.paineladmin, name = "painel"),
    path('adicionarcurso/', views.adicionarcurso, name='adicionarcurso'),
    path('editarcurso/<int:id_curso>/', views.editarcurso, name='editarcurso'),
    path('removercurso/<int:id_curso>/', views.removercurso, name='removercurso'),
    path('adicionarvinculo/', views.adicionarvinculo, name='adicionarvinculo'),
    path('editarvinculo/<int:id_vinculo>/', views.editarvinculo, name='editarvinculo'),
    path('removervinculo/<int:id_vinculo>/', views.removervinculo, name='removervinculo'),
]
