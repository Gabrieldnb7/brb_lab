from django.contrib import admin
from .models import Eventos

from django.urls import path, reverse
from django.http import HttpResponse
import qrcode
import io

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'horario', 'ambiente', 'download_qrcode_button', 'ativo', 'criado_em')
    list_filter = ('data', 'criado_em')
    search_fields = ('titulo', 'descricao', 'palestrantes', 'ambiente')

    exclude = ('id_usuario', 'checkin_code', 'criado_em', 'total_inscritos')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/download_qrcode', self.admin_site.admin_view(self.download_qrcode), name='download_qrcode')
        ]
        return custom_urls + urls
    
    def download_qrcode(self, request, object_id):
        checkin = self.get_object(request, object_id)
        if not checkin:
            return HttpResponse(status=404)

        qr = qrcode.make(checkin.checkin_code)
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)

        response = HttpResponse(buffer, content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="qrcode_{checkin.checkin_code}.png"'
        return response
    
    def download_qrcode_button(self, obj):
        from django.utils.html import format_html
        url = reverse('admin:download_qrcode', args=[obj.pk])
        return format_html('<a class="button" href="{}">Baixar QR Code</a>', url)
    
    download_qrcode_button.short_description = 'QR Code'
    download_qrcode_button.allow_tags = True

    @admin.display(boolean=True, description='Ativo')
    def ativo(self, obj):
        
        return obj.ativo

    def save_model(self, request, obj, form, change):
        if not change:
            obj.id_usuario = request.user
        obj.save()