from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import UserRegistrationForm, UserLoginForm
from .models import Usuario

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

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
                password=form.cleaned_data['senha']
            )
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('/login')
        else:
            messages.error(request, f"Erros no formulário: {form.errors}")

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
                return redirect('/')

    return render(request, 'login.html', {'form': form})
                

def logout(request):
    auth.logout(request)
    return redirect('home')
