from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse
from .forms import UserRegistrationForm, UserLoginForm, UserProfileEditForm
from .models import Usuario

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Alterações salvas com sucesso!")
            return redirect(reverse("users:perfil"))
        else:
            messages.error(request, "Falha ao salvar as alterações")
            return redirect(reverse("users:perfil"))
    else:
        form = UserProfileEditForm(instance=request.user)
    return render(request, 'profile.html', { 'form' : form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            Usuario.objects.create_user(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                cpf=form.cleaned_data['cpf'],
                telefone=form.cleaned_data['telefone'],
                lotacao=form.cleaned_data.get('lotacao'),
                matricula=form.cleaned_data.get('matricula'),
                tipo_usuario='cliente',
                password=form.cleaned_data['password1']
            )
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('users:login')
        else:
            messages.error(request, f"Erro nos campos de cadastro, tente novamente.")

    else:
        form = UserRegistrationForm()
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    form = UserLoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            password = form.cleaned_data['senha']

            user = auth.authenticate(request, cpf=cpf, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Login feito com sucesso!")
                return redirect('access:home')
            else:
                messages.error(request, "Erro ao efetuar login, tente novamente.")
                return redirect('users:login')

    return render(request, 'login.html', {'form': form})
                

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout feito com sucesso!")
    return redirect('access:home')
