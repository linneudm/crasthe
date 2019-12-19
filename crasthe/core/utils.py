import re

def cnpj_hashdigit(cnpj, position):  # type: (str, int) -> int
    """
    Will compute the given `position` checksum digit for the `cnpj`
    input. The input needs to contain all elements previous to
    `position` else computation will yield the wrong result.
    """
    weightgen = chain(range(position -8, 1, -1), range(9, 1, -1))
    val = sum(int(digit) * weight for digit, weight in zip(cnpj, weightgen)) % 11
    return 0 if val < 2 else 11 - val

def validate_cnpj(cnpj):  # type: (str) -> bool
	cnpj = re.sub('\D', '', cnpj)
	print(cnpj)
	"""
	Returns whether or not the verifying checksum digits of the
	given `cnpj` match it's base number. Input should be a digit
	string of proper length.
	"""
	if not cnpj.isdigit() or len(cnpj) != 14 or len(set(cnpj)) == 1: return False
	return all(cnpj_hashdigit(cnpj, i +13) == int(v) for i, v in enumerate(cnpj[12:]))

def cpf_hashdigit(cpf, position):  # type: (str, int) -> int
    """
    Will compute the given `position` checksum digit for the `cpf`
    input. The input needs to contain all elements previous to
    `position` else computation will yield the wrong result.
    """
    val = sum(int(digit) * weight for digit, weight in zip(cpf, range(position, 1, -1))) % 11
    return 0 if val < 2 else 11 - val

def validate_cpf(cpf):  # type: (str) -> bool
	cpf = re.sub('\D', '', cpf)
	print(cpf)
	"""
	Returns whether or not the verifying checksum digits of the
	given `cpf` match it's base number. Input should be a digit
	string of proper length.
	"""
	if not cpf.isdigit() or len(cpf) != 11 or len(set(cpf)) == 1: return False
	return all(cpf_hashdigit(cpf, i +10) == int(v) for i, v in enumerate(cpf[9:]))