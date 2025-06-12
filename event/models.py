from django.db import models
from django.utils.timezone import now
from users.models import Usuario 


class Eventos(models.Model):
        
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=45)
    data = models.DateField()
    horario = models.CharField(max_length=45)
    ambiente = models.CharField(max_length=45)
    descricao = models.CharField(max_length=500)
    palestrantes = models.CharField(max_length=45)
    checkin_code = models.CharField(max_length=45, null=True, blank=True)
    total_inscritos = models.IntegerField()
    criado_em = models.DateTimeField(default=now)

    def __str__(self):
        return self.titulo
    
    @property
    def ativo(self):
        return self.data >= now().date()

class Inscricao(models.Model):
    id_inscricao = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')
    id_evento = models.CharField(max_length=45, db_column='id_evento')  # Substitua por ForeignKey(Evento) no futuro
    criadoEm = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'inscricoes'

    def __str__(self):
        return f"Inscrição #{self.id_inscricao} de {self.usuario.nome}"
