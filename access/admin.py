from django.contrib import admin
from .models import Acesso

@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    readonly_fields = ['idAcesso', 'usuario', 'Ambiente', 'criadoEm']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False