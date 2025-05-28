from django import forms
from .validators import validate_cpf
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UserRegistrationForm(UserCreationForm):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email")
    cpf = forms.CharField(label="CPF", max_length=11, validators=[validate_cpf])
    telefone = forms.CharField(label="Telefone", max_length=20)
    lotacao = forms.CharField(label="Lotação", required=False)
    matricula = forms.CharField(label="Matrícula", required=False)

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'cpf', 'telefone', 'lotacao', 'matricula', 'password1', 'password2')

class UserLoginForm(forms.Form):
    
    cpf = forms.CharField(max_length=14, required=True, validators=[validate_cpf])
    senha = forms.CharField(required=True)
