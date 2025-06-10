from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import Usuario
from .validators import validate_cpf

class UserRegistrationForm(UserCreationForm):
    nome = forms.CharField(label="Nome Completo",
                           max_length=100,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Seu nome completo'}))
    email = forms.EmailField(label="Email Principal",
                             widget=forms.EmailInput(attrs={
                                'placeholder': 'email@website.com'}))
    cpf = forms.CharField(label="CPF",
                        max_length=14, 
                        validators=[validate_cpf],
                        widget=forms.TextInput(attrs={
                            'placeholder': '000.000.000-00'}))
    telefone = forms.CharField(label="Telefone Celular",
                            max_length=20, required=False,
                            widget=forms.TextInput(attrs={
                            'placeholder': '(XX) XXXXX-XXXX'}))
    lotacao = forms.CharField(label="Lotação (Opcional)",
                            max_length=100,
                            required=False)
    matricula = forms.CharField(label="Matrícula (Opcional)", 
                            max_length=50, 
                            required=False)


    class Meta(): 
        model = Usuario        
        fields = ('nome', 'email', 'cpf', 'telefone', 'lotacao', 'matricula', 'password1', 'password2')


class UserLoginForm(forms.Form):
    cpf = forms.CharField(label="CPF", max_length=14, required=True, validators=[validate_cpf],
                          widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Seu CPF'}))
    senha = forms.CharField(label="Senha", required=True,
                            widget=forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Sua senha'}))
    
class UserProfileEditForm(forms.ModelForm):
    lotacao = forms.CharField(
        label="Lotação",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome = forms.CharField(
        label="Nome Completo",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email Principal",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    telefone = forms.CharField(
        label="Telefone Celular",
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': '(XX) XXXXX-XXXX'})
    )
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'telefone', 'lotacao')

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
    
