from django import forms

class UserRegistrationForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email")
    cpf = forms.CharField(label="CPF", max_length=11)
    telefone = forms.CharField(label="Telefone", max_length=20)
    lotacao = forms.CharField(label="Lotação", required=False)
    matricula = forms.CharField(label="Matrícula", required=False)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

def clean_cpf(self):
    cpf = self.cleaned_data['cpf']
    
    cpf = cpf.replace('.', '').replace('-', '')
    
    if not cpf.isdigit() or len(cpf) != 11:
        raise forms.ValidationError("O CPF deve conter exatamente 11 dígitos numéricos.")
    
    return cpf
