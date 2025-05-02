from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        nome         = request.POST.get('nome')
        email        = request.POST.get('email')
        cpf          = request.POST.get('cpf')
        telefone     = request.POST.get('telefone')
        lotacao      = request.POST.get('lotacao') or None
        matricula    = request.POST.get('matricula') or None
        tipo_usuario = request.POST.get('tipo_usuario')
        senha_raw    = request.POST.get('senha')
        
        # Verificações básicas
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF já cadastrado.')
            return render(request, 'register.html')
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return render(request, 'register.html')

        # Criptografa a senha
        senha_hash = make_password(senha_raw)

        Usuario.objects.create(
            nome=nome,
            email=email,
            cpf=cpf,
            telefone=telefone,
            lotacao=lotacao,
            matricula=matricula,
            tipo_usuario=tipo_usuario,
            senha=senha_hash
        )

        messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
        return redirect('login')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
