from django.urls import path
from access.views import home, registrar_acesso
from . import views
    
app_name = 'access'

urlpatterns = [
    path('', home, name='home'),
    path('checkin', registrar_acesso, name='scanner'),
    path('meus_acessos', views.meus_acessos, name='meus_acessos'),
]