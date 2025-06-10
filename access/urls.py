from django.urls import path
from access.views import home, registrar_acesso

app_name = 'access'

urlpatterns = [
    path('', home, name='home'),
    path('checkin', registrar_acesso, name='scanner'),
]