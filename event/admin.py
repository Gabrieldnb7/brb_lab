from django.contrib import admin
from .models import Eventos

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'horario', 'ambiente', 'ativo', 'total_inscritos', 'criado_em')
    list_filter = ('data', 'criado_em')
    search_fields = ('titulo', 'descricao', 'palestrantes', 'ambiente')

    @admin.display(boolean=True, description='Ativo')
    def ativo(self, obj):
        
        return obj.ativo