from django.urls import path
from . import views

urlpatterns = [
    # === ROTA NOVA: remover inscrição ===
    path(
        "eventos/<int:id_evento>/cancelar/",
        views.remover_inscricao,
        name="remover_inscricao",
    ),
]

from django.urls import path
from event.views import events, myEvents, registerUser

app_name = 'event'

urlpatterns = [
    path('eventos', events, name='eventos'),
    path('meusEventos', myEvents, name='meusEventos'),
    path('inscrever/<int:id_evento>/', registerUser, name='inscrever'),
    path("eventos/<int:id_evento>/cancelar/", remover_inscricao, name="remover_inscricao"),
]