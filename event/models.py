from django.db import models
from django.utils import timezone

class Eventos(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=45)
    data = models.DateField()
    horario = models.CharField(max_length=45)
    ambiente = models.CharField(max_length=45)
    descricao = models.CharField(max_length=500)
    palestrantes = models.CharField(max_length=45)
    checkin_code = models.CharField(max_length=45, null=True, blank=True)
    status = models.CharField(max_length=45)
    total_inscritos = models.IntegerField()
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
