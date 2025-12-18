from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('cadastre-se/', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('sair/', views.sair, name='sair'),
    path('users/', views.users, name='users'), 
    path("users/<int:user_id>/toggle/", views.toggle_superuser, name="toggle_superuser"),
]