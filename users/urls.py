from django.urls import path
from users.views import login, register, logout, profile

app_name = 'users'

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', register, name='cadastro'),
    path('logout', logout, name='logout'),
    path('perfil', profile, name='perfil')
]