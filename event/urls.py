
from django.urls import path
from event.views import events, myEvents, registerInEvent, unsubscribe, eventDescription

app_name = 'event'

urlpatterns = [
    path('eventos', events, name='eventos'),
    path('meusEventos', myEvents, name='meusEventos'),
    path('eventos/descricao/<int:id_evento>/', eventDescription, name='descricao'),
    path('inscrever/<int:id_evento>/', registerInEvent, name='inscrever'),
    path("eventos/<int:id_evento>/cancelar/", unsubscribe, name="remover_inscricao"),
]