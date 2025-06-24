from django.db import models
from users.models import Usuario

class Acesso(models.Model):
    idAcesso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,db_column='id_usuario',on_delete=models.CASCADE)
    Ambiente = models.CharField(max_length=45)
    criadoEm = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'acesso'

    def __str__(self):
        return f"{self.usuario.nome} - {self.Ambiente}"
