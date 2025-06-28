from django.db import models
from django.utils.timezone import now
from users.models import Usuario 
import uuid

class Eventos(models.Model):
    id_evento = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=45)
    data = models.DateField()
    horario = models.CharField(max_length=45)
    ambiente = models.CharField(max_length=45)
    descricao = models.TextField(max_length=500)
    palestrantes = models.CharField(max_length=45)
    checkin_code = models.UUIDField(default=uuid.uuid4, editable=False)
    total_inscritos = models.IntegerField(default=0)
    criado_em = models.DateTimeField(default=now)

    def __str__(self):
        return self.titulo
    
    @property
    def ativo(self):
        return self.data >= now().date()
    
class TipoInscricao(models.TextChoices):
    ACTIVE = ('ativa', 'Ativa')
    CANCELED = ('cancelada', 'Cancelada')
    VALIDATED = ('validada', 'Validada')
    EXPIRED = ('expirada', 'Expirada')

class Inscricao(models.Model):
    id_inscricao = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, db_column='id_evento')
    criadoEm = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=TipoInscricao.choices, default=TipoInscricao.ACTIVE)

    class Meta:
        db_table = 'inscricoes'

    def __str__(self):
        return f"Inscrição #{self.id_inscricao} de {self.usuario.nome}"
