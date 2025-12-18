from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import User
from .forms import CadastroForm
from django.http import JsonResponse

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



@login_required
@staff_member_required
def toggle_superuser(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)
    
    if user.pk == 1:
        return redirect('users')
    
    if request.method == "POST":
        user.is_superuser = not user.is_superuser
        user.is_staff = not user.is_staff
        user.save()
    
    return redirect('users')