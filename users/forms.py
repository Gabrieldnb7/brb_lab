from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import Usuario
from .validators import validate_cpf
import re

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
                            'placeholder': '000.000.000-00',
                            'id': 'exampleInputCPF1'}))
    telefone = forms.CharField(label="Telefone Celular",
                            max_length=20, required=False,
                            widget=forms.TextInput(attrs={
                            'placeholder': '(XX) XXXXX-XXXX',
                            'id': 'exampleInputTel1'}))
    lotacao = forms.CharField(label="Lotação (Opcional)",
                            max_length=100,
                            required=False)
    matricula = forms.CharField(label="Matrícula (Opcional)", 
                            max_length=50, 
                            required=False)
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if cpf:
            cpf = re.sub(r'\D', '', cpf)        
        return cpf

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        if not matricula:
            return None
        return matricula
    
    def clean_lotacao(self):
        lotacao = self.cleaned_data.get('lotacao')
        if not lotacao:
            return None
        return lotacao
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get("telefone")
        if telefone:
            telefone = re.sub(r'\D', '', telefone)
            if len(telefone) != 11:
                raise forms.ValidationError("O telefone deve ter 11 dígitos (incluindo DDD).")
        return telefone

    class Meta(): 
        model = Usuario        
        fields = ('nome', 'email', 'cpf', 'telefone', 'lotacao', 'matricula', 'password1', 'password2')


class UserLoginForm(forms.Form):
    cpf = forms.CharField(label="CPF", max_length=14, required=True, validators=[validate_cpf],
                          widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Seu CPF'}))
    senha = forms.CharField(label="Senha", required=True,
                            widget=forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Sua senha'}))
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if cpf:
            cpf = re.sub(r'\D', '', cpf)        
        return cpf
        
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
    
