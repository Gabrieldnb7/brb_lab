from django.urls import path
from access.views import home, scanner

app_name = 'access'

urlpatterns = [
    path('', home, name='home'),
    path('checkin', scanner, name='scanner'),
]