from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Eventos, Inscricao
from users.models import Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def event(request):
    return render(request, 'event.html')

def events(request):
    eventos = Eventos.objects.all()
    return render(request, 'events.html', {'eventos': eventos})

def myEvents(request):
    return render(request, 'myEvents.html')

def inscrever_usuario(request, id_evento):
    if not request.user.is_authenticated:
        return redirect('login')  # se não estiver logado, redireciona

    evento = get_object_or_404(Eventos, pk=id_evento)

    # Verifica se já está inscrito
    if Inscricao.objects.filter(usuario=request.user, id_evento=id_evento).exists():
        return render(request, 'inscricao_existente.html', {'evento': evento})

    inscricao = Inscricao.objects.create(
        usuario=request.user,
        id_evento=id_evento,
        status=1
    )

    return render(request, 'inscricao_sucesso.html', {'evento': evento})