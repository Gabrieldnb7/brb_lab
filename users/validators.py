from django.core.exceptions import ValidationError
import re

def validate_cpf(value):
    
    def calculate_digit(digits):
        s = sum(int(d)*w for d, w in zip(digits, range(len(digits)+1, 1, -1)))
        rest = (s * 10) % 11
        return '0' if rest == 10 else str(rest)
    
    cpf = re.sub(r'[^0-9]', '', value)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido.')
    
    if cpf[9] != calculate_digit(cpf[:9]) or cpf[10] != calculate_digit(cpf[:10]):
        raise ValidationError('CPF inválido.')
    
