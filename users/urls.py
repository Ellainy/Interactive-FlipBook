from django.urls import path
from . import views

urlpatterns = [
    path('cadastre-se/', views.cadastro, name='cadastro'),
    path('perfil/', views.profile, name='perfil'),
    path('editarPerfil/', views.editar, name='editarPerfil'),
]