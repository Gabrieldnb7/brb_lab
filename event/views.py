from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def event(request):
    return render(request, 'event.html')

def events(request):
    return render(request, 'events.html')

def myEvents(request):
    return render(request, 'myEvents.html')

def eventos_ativos(request):
    eventos = Evento.objects.filter(status=1) 
    return render(request, 'eventos_ativos.html', {'eventos': eventos})