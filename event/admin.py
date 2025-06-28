from django.contrib import admin
from .models import Eventos

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'horario', 'ambiente', 'ativo', 'criado_em')
    list_filter = ('data', 'criado_em')
    search_fields = ('titulo', 'descricao', 'palestrantes', 'ambiente')

    exclude = ('id_usuario', 'checkin_code', 'criado_em', 'total_inscritos')

    @admin.display(boolean=True, description='Ativo')
    def ativo(self, obj):
        
        return obj.ativo

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id_usuario = request.user
        obj.save()