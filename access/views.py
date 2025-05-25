# access/views.py
import os

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt        # remova se usar CSRF normal
from django.contrib.auth.decorators import login_required

from .models import Acesso                                   # modelo deste app

# ======= Páginas simples que já existiam =======
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

# ======= NOVA VIEW PARA REGISTRAR ACESSO =======
@csrf_exempt            # deixe apenas se o scanner não enviar CSRF-token
@require_POST
@login_required         # retire se não exigir que o usuário esteja logado
def registrar_acesso(request):
    """
    Espera POST com:
        - codigo   : string lida do QRCode
        - ambiente : nome do ambiente escolhido no dropdown
    Valida 'codigo' contra VERIFY_CODE definido no .env
    e cria um novo registro na tabela Acesso.
    """
    codigo   = request.POST.get('codigo')
    ambiente = request.POST.get('ambiente')

    # validações básicas
    if not codigo or not ambiente:
        return JsonResponse(
            {'erro': 'codigo e ambiente são obrigatórios'}, status=400)

    verify_code = os.getenv('VERIFY_CODE')         # definido em .env
    if codigo != verify_code:
        return JsonResponse({'erro': 'código inválido'}, status=401)

    # grava no banco
    acesso = Acesso.objects.create(
        usuario=request.user,                      # FK para usuário logado
        Ambiente=ambiente
    )

    return JsonResponse(
        {'mensagem': 'Acesso registrado', 'idAcesso': acesso.idAcesso},
        status=201
    )
