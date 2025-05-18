from django import forms
from .validators import validate_cpf

class UserRegistrationForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email")
    cpf = forms.CharField(label="CPF", max_length=11, validators=[validate_cpf])
    telefone = forms.CharField(label="Telefone", max_length=20)
    lotacao = forms.CharField(label="Lotação", required=False)
    matricula = forms.CharField(label="Matrícula", required=False)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    
    cpf = forms.CharField(max_length=14, required=True, validators=[validate_cpf])
    senha = forms.CharField(required=True)
