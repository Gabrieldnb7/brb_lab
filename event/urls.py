from django.urls import path
from event.views import events, myEvents, registerUser

app_name = 'event'

urlpatterns = [
    path('eventos', events, name='eventos'),
    path('meusEventos', myEvents, name='meusEventos'),
    path('inscrever/<int:id_evento>/', registerUser, name='inscrever'),
]