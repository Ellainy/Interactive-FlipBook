from django.urls import path
from . import views

urlpatterns = [
    path('cadastre-se/', views.register, name='register'),
    path('perfil/', views.profile, name='perfil'),
    path('editarPerfil/', views.editar, name='editarPerfil'),
]