from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=45, unique=False)
    cpf = models.CharField(max_length=11, unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    lotacao = models.CharField(max_length=45, null=True, blank=True)
    matricula = models.CharField(max_length=6, unique=True, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=15, help_text='Haverá uma hierarquia de acessos')

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nome} ({self.email})"