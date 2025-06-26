from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm
from .models import Usuario

# Register your models here.
class UsuarioAdmin(UserAdmin):
    add_form = UserRegistrationForm
    model = Usuario
    list_display = ("cpf", "nome", "email", "tipo_usuario", "is_active", "is_staff")
    ordering = ("nome",)

    fieldsets = (
        (None, {"fields": ("cpf", "password")}),
        ("Informações pessoais", {"fields": ("nome", "email", "telefone", "matricula", "lotacao", "tipo_usuario")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("cpf", "nome", "email", "password", "telefone", "matricula", "lotacao", "tipo_usuario", "is_active", "is_staff"),
        }),
    )

    search_fields = ("cpf", "nome", "email")

admin.site.register(Usuario, UsuarioAdmin)