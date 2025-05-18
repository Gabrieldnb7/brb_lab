from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, nome, cpf, email, password=None, **extra_fields):
        if not cpf:
            raise ValueError("O CPF é obrigatório.")
        
        email = self.normalize_email(email)
        user = self.model(cpf=cpf, nome=nome, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, cpf, nome, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(cpf, nome, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=45, unique=False)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11)
    lotacao = models.CharField(max_length=45, null=True, blank=True)
    matricula = models.CharField(max_length=6, unique=True, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=15, help_text='Haverá uma hierarquia de acessos')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome', 'email']

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nome} ({self.email})"