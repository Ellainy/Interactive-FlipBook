from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/', views.livro, name='livro'),
    path('sobre/', views.sobre, name='sobre'),
    path('lerlivro/', views.lerlivro, name='lerlivro'),
    path('admin2/', views.admin, name='administracao'),
]