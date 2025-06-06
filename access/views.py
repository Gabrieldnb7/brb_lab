# access/views.py
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Acesso


# ---- páginas simples que já existiam ----------------------------------
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


# ---- nova view para registrar acesso ----------------------------------
@csrf_exempt            # remova se usar CSRF normal
@require_POST
@login_required         # retire se não exigir login
def registrar_acesso(request):
    """
    Espera POST com:
        - codigo   : string lida do QRCode
        - ambiente : nome do ambiente escolhido no dropdown
    Valida 'codigo' contra VERIFY_CODE definido no .env
    e cria um novo registro em Acesso.
    """
    codigo = request.POST.get('codigo')
    ambiente = request.POST.get('ambiente')

    # validações básicas
    if not codigo or not ambiente:
        return HttpResponse('codigo e ambiente são obrigatórios', status=400)

    verify_code = os.getenv('VERIFY_CODE')
    if codigo != verify_code:
        return HttpResponse('código inválido', status=401)

    # grava no banco
    acesso = Acesso.objects.create(
        usuario=request.user,      # FK do usuário logado
        Ambiente=ambiente
    )

    return HttpResponse(
        f'Acesso registrado – idAcesso={acesso.idAcesso}',
        status=201
    )
