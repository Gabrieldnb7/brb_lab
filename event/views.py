from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Eventos, Inscricao
from users.models import Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def events(request):
    eventos = Eventos.objects.all()
    return render(request, 'events.html', {'eventos': eventos})

def myEvents(request):
    eventos = Eventos.objects.filter(inscricao__usuario=request.user)
    return render(request, 'myEvents.html', {'eventos': eventos})

def eventsDescricao(request, id_evento):
    evento = get_object_or_404(Eventos, pk=id_evento)
    return render(request, 'events.html', {'evento': evento}) 

def registerUser(request, id_evento):
    if not request.user.is_authenticated:
        return redirect('login')
    evento = get_object_or_404(Eventos, pk=id_evento)
    if Inscricao.objects.filter(usuario=request.user, id_evento=id_evento).exists():
        return render(request, 'inscricao_existente.html', {'evento': evento})
    inscricao = Inscricao.objects.create(
        usuario=request.user,
        id_evento=id_evento,
        status=1
    )
    return render(request, 'inscricao_sucesso.html', {'evento': evento})


@login_required
def unsubscribe(request, id_evento):
    inscricao = get_object_or_404(
        Inscricao,
        usuario=request.user,
        id_evento=id_evento
    )

    if request.method == "POST":
        inscricao.delete()
        messages.success(request, "Inscrição removida com sucesso!")
        return redirect("events.html")  

    evento = get_object_or_404(Eventos, pk=id_evento)
    return render(request, "confirmar_remocao.html", {"evento": evento})

def eventDescription(request):
    return render(request, 'eventDescription.html')