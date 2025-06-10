from django.urls import path
from access.views import home

app_name = 'access'

urlpatterns = [
    path('', home, name='home'),
]