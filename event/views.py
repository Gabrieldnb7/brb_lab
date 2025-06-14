from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Eventos, Inscricao
from users.models import Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date

def events(request):
    eventos = Eventos.objects.all()
    return render(request, 'events.html', {'eventos': eventos})

def myEvents(request):
    if not request.user.is_authenticated:
        return redirect('login')
    inscricoes = Inscricao.objects.filter(usuario=request.user).select_related('id_evento')
    context = {
        'inscricoes': inscricoes,
        'today': date.today()
    }
    return render(request, 'myEvents.html',context)
    

def eventsDescricao(request):
    eventos = Eventos.objects.all()
    # return render(request, 'myEvents.html', {'eventos': eventos})
    return render(request, 'events.html', {'eventos': eventos}) #aba descrição

def registerInEvent(request, id_evento):
    if not request.user.is_authenticated:
        return redirect('login')
    
    evento = get_object_or_404(Eventos, pk=id_evento)

    if Inscricao.objects.filter(usuario=request.user, id_evento=evento).exists():
        return render(request, 'inscricao_existente.html', {'evento': evento})
    inscricao = Inscricao.objects.create(
        usuario=request.user,
        id_evento=evento,
        status=1
    )
    evento.total_inscritos += 1
    evento.save()
    return render(request, 'inscricao_sucesso.html', {'evento': evento})


@login_required
def unsubscribe(request, id_evento):
    if not request.user.is_authenticated:
        return redirect('login')
    
    evento = get_object_or_404(Eventos, pk=id_evento)
    
    # Verificar se o usuário está inscrito
    inscricao = get_object_or_404(Inscricao, usuario=request.user, id_evento=evento)
    
    if request.method == 'POST':
        # Cancelar a inscrição
        inscricao.delete()
        
        # Opcional: Diminuir o total de inscritos
        if evento.total_inscritos > 0:
            evento.total_inscritos -= 1
            evento.save()
        
        # Redirecionar com mensagem de sucesso
        messages.success(request, f'Sua inscrição no evento "{evento.titulo}" foi cancelada com sucesso.')
        return redirect('event:meusEventos')
    
    return render(request, 'confirmar_remocao.html', {'evento': evento})

def eventDescription(request):
    return render(request, 'eventDescription.html')