#from crasthe.core import validators
from django.core.exceptions import ValidationError

def validate_cpfcnpj(value):
    if len(value) != 11 or len(value) != 14:
        raise ValidationError('CPF/CNPJ nao e valido.')
    elif len(value) == 11:
    	if(not validate_cpf(value)):
        	raise ValidationError('CPF/CNPJ nao eh valido.')
    else:
    	if(not validate_cnpj(value)):
        	raise ValidationError('CPF/CNPJ nao eh valido.')
    return True

def validate_bairro(value):
	raise ValidationError('CPF/CNPJ nao eh valido.')
