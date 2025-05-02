from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from .forms import UserRegistrationForm
from .models import Usuario


# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            Usuario.objects.create(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                cpf=form.cleaned_data['cpf'],
                telefone=form.cleaned_data['telefone'],
                lotacao=form.cleaned_data.get('lotacao'),
                matricula=form.cleaned_data.get('matricula'),
                tipo_usuario='cliente',
                senha=form.cleaned_data['senha']
            )
            return HttpResponse("Usuário registrado com sucesso!")
        else:
            return HttpResponse(f"Erros no formulário: {form.errors}", status=400)

    else:
        return HttpResponse("Apenas POST é permitido.", status=405)


def logout(request):
    auth.logout(request)
    return redirect('home')
