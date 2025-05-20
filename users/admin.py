from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm
from .models import Usuario

# Register your models here.
class UsuarioAdmin(UserAdmin):
    add_form = UserRegistrationForm
    model = Usuario
    list_display = ("cpf", "nome")
    ordering = ("nome",)

admin.site.register(Usuario, UsuarioAdmin)