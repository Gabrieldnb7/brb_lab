"""
URL configuration for brblab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# brblab/urls.py

from django.contrib import admin
from django.urls import path

# ====== imports das views ======
from access.views import home, registrar_acesso
from users.views import profile, register, login
from event.views import (
    events,
    myEvents,
    event,
    inscrever_usuario,
    remover_inscricao,   # ← importe a nova view aqui
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # páginas principais
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('cadastro/', register, name='register'),
    path('perfil/', profile, name='profile'),

    # eventos
    path('eventos/', events, name='events'),
    path('meusEventos/', myEvents, name='myEvents'),
    path('evento/', event, name='event'),
    path('inscrever/<int:id_evento>/', inscrever_usuario, name='inscrever_usuario'),

    # === ROTA NOVA: remover inscrição do usuário de um evento ===
    path(
        'eventos/<int:id_evento>/cancelar/',
        remover_inscricao,
        name='remover_inscricao',
    ),

    # ====== nova rota para registrar acesso ======
    path('acesso/', registrar_acesso, name='registrar_acesso'),
]
