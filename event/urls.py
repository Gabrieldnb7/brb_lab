from django.urls import path
from event.views import events, myEvents, registerUser, unsubscribe, eventDescription

app_name = 'event'

urlpatterns = [
    path('eventos', events, name='eventos'),
    path('meusEventos', myEvents, name='meusEventos'),
    path('eventos/descricao/<int:id_evento>', eventDescription, name='descricao'), 
    path('eventos/inscrever/<int:id_evento>', registerUser, name='inscrever'),
    path("eventos/cancelar/<int:id_evento>", unsubscribe, name="remover_inscricao"),
]