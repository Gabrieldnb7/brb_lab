from django import template
import re

register = template.Library()

@register.filter(name='mask_cpf')
def mask_cpf(value):
    if not value:
        return ""
    cpf_limpo = re.sub(r'\D', '', str(value))
    if len(cpf_limpo) != 11:
        return value 
    return f'{cpf_limpo[:3]}.***.***-{cpf_limpo[-2:]}'
