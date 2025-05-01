from django.db import models
from users import Usuario  

class Inscricao(models.Model):
    id_inscricao = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='IdUsuario')
    id_evento = models.CharField(max_length=45, db_column='IdEvento')  # Substitua por ForeignKey(Evento) no futuro

    class Meta:
        db_table = 'inscricoes'

    def __str__(self):
        return f"Inscrição #{self.id_inscricao} de {self.usuario.nome}"

