# access/views.py
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Acesso

def home(request):
    return render(request, 'home.html')

@csrf_exempt            # remova se usar CSRF normal
@require_POST
@login_required         
def registrar_acesso(request):
    codigo = request.POST.get('codigo')
    ambiente = request.POST.get('ambiente')

    if not codigo or not ambiente:
        return HttpResponse('codigo e ambiente são obrigatórios', status=400)

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
