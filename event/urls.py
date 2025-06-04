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
