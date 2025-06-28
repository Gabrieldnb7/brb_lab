from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Eventos, Inscricao, TipoInscricao
from users.models import Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
import json
from django.core.exceptions import ValidationError


def events(request):
    eventos = Eventos.objects.all()

    if request.user.is_authenticated:
        print('ta on')
        inscricoes = Inscricao.objects.filter(usuario=request.user)

        for event in eventos:
            event.inscrito = event in map(lambda x: x.id_evento, inscricoes)

    else:
        for event in eventos:
            event.inscrito = False

    return render(request, 'events.html', {'eventos': eventos})

@login_required
def myEvents(request):
    if not request.user.is_authenticated:
        return redirect('login')
    inscricoes = Inscricao.objects.filter(usuario=request.user).select_related('id_evento')
    context = {
        'inscricoes': inscricoes,
        'today': date.today()
    }
    return render(request, 'myEvents.html',context)
    
@login_required
def eventDescription(request, id_evento):  # ← Recebe id_evento
    if not request.user.is_authenticated:
        return redirect('login')
    
    evento = get_object_or_404(Eventos, pk=id_evento)
    
    return render(request, 'eventDescription.html', {'evento': evento})

@login_required
def registerInEvent(request, id_evento):
    if not request.user.is_authenticated:
        return redirect('login')
    
    evento = get_object_or_404(Eventos, pk=id_evento)

    if Inscricao.objects.filter(usuario=request.user, id_evento=evento).exists():
        return render(request, 'inscricao_existente.html', {'evento': evento})
    inscricao = Inscricao.objects.create(
        usuario=request.user,
        id_evento=evento,
        status=TipoInscricao.ACTIVE
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

@csrf_exempt           
@login_required         
def validar_inscricao(request, id_evento):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(json.dumps({"erro": "JSON inválido"}), status=400)

        codigo = data.get('codigo')

        if not codigo:
            return HttpResponse(json.dumps({"erro": 'O código da inscrição é obrigatório'}), status=400)

        try:
            print(id_evento, codigo)
            evento = Eventos.objects.get(pk=id_evento, checkin_code=codigo)
        except(Eventos.DoesNotExist, ValidationError):
            return HttpResponse(json.dumps({"erro": 'Código inválido'}), status=400)
        
        try:
            inscricao = Inscricao.objects.get(usuario=request.user, id_evento=evento.id_evento)
        except(Inscricao.DoesNotExist):
            return HttpResponse(json.dumps({"erro": 'Você não está inscrito neste evento'}), status=404)

        if inscricao.status != TipoInscricao.ACTIVE:
            return HttpResponse(json.dumps({"erro": f'Sua inscrição neste evento foi {inscricao.status}'}), status=404)
        
        inscricao.status = TipoInscricao.VALIDATED
        inscricao.save()

        return HttpResponse(
            f'Inscricão validada com sucesso – idAcesso={inscricao.id_inscricao}',
            status=202
        )
    
    try:
        evento = Eventos.objects.get(id_evento=id_evento)
    except Eventos.DoesNotExist:
        return redirect('event:meusEventos')
    return render(request, 'sub-scanner.html', {'evento': evento})