from django.contrib.auth.backends import ModelBackend
from .models import Usuario

class CPFBackend(ModelBackend):
    def authenticate(self, request, cpf=None, password=None, **kwargs):
        try:
            user = Usuario.objects.get(cpf=cpf)
            if user.check_password(password):
                return user
        except Usuario.DoesNotExist:
            return None
