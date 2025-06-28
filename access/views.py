import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from event.models import Eventos
from django.utils import timezone
import json

from .models import Acesso

def home(request):
    data_de_hoje = timezone.now().date()
    evento_destaque = None
    evento_destaque = Eventos.objects.filter(
        data__gte=data_de_hoje
    ).order_by('data').first()

    return render(request, 'home.html', {"evento_destaque" : evento_destaque})

@csrf_exempt           
@login_required         
def registrar_acesso(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse("JSON inválido", status=400)

        codigo = data.get('codigo')
        ambiente = data.get('ambiente')

        if not codigo or not ambiente:
            return HttpResponse('Código e ambiente são obrigatórios', status=400)

        verify_code = os.getenv('VERIFY_CODE')
        if codigo != verify_code:
            return HttpResponse('código inválido', status=401)

        acesso = Acesso.objects.create(
            usuario=request.user,      
            Ambiente=ambiente
        )

        return HttpResponse(
            f'Acesso registrado – idAcesso={acesso.idAcesso}',
            status=201
        )
    
    return render(request, 'scanner.html')
