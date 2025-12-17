from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import User
from django.utils import timezone
from .forms import CadastroForm

def first_superuser(request):
    user = User.objects.get(pk=1)
    user.is_superuser = True
    user.is_staff = True
    user.save()

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            first_superuser(request)
            return redirect('login')
    else:
        form = CadastroForm()
    
    context = {'form': form}
    return render(request, 'registration/cadastro.html', context)

def sair(request):
    logout(request)
    return redirect('index')


@staff_member_required
def users(request):
  
    usuarios = User.objects.all().order_by('date_joined')
    
    
    lista_usuarios = []
    for usuario in usuarios:
        
        lista_usuarios.append({
            'id': usuario.id,
            'username': usuario.username,
            'email': usuario.email,
            'data_cadastro': usuario.date_joined.strftime('%d/%m/%Y'), 
            'is_staff': usuario.is_staff,
            'is_superuser': usuario.is_superuser,
        })
 

    context = {
        'usuarios': lista_usuarios,
        'total_usuarios': len(lista_usuarios),
    }
    
    return render(request, 'users.html', context)