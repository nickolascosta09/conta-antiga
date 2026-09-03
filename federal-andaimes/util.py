def validar_cpf(cpf):
    cpf1 = ''.join(filter(str.isdigit, cpf))
    if len(cpf1) != 11:
        print("Erro! CPF informado tem menos de 11 dígitos")
        return False
    if cpf1 == cpf1[0] * 11:
        print("Erro! Esse CPF não é válido")
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf1[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if int(cpf1[9]) != digito1:
        return False
    soma = 0
    for i in range(10):
        soma += int(cpf1[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if int(cpf1[10]) != digito2:
        return False
    return True

def validar_cnpj(cnpj):
    cnpj1 = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj1) != 14:
        return False
    if cnpj1 == cnpj1[0] * 14:
        return False
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i in range(12):
        soma += int(cnpj1[i]) * pesos1[i] 
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if int(cnpj1[12]) != digito1:
        return False
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    for i in range(13):
        soma += int(cnpj1[i]) * pesos2[i]
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if int(cnpj1[13]) != digito2:
        return False
    return True

def validar_documento(documento):
    numeros = ''.join(filter(str.isdigit, documento))
    if len(numeros) == 11:
        return validar_cpf(numeros)
    elif len(numeros) == 14:
        return validar_cnpj(numeros)
    else:
        print("Erro! Documento não é válido")
        return False

def aplicar_mascara(texto):
    numeros = ''.join(filter(str.isdigit, texto))
    if len(numeros) > 14:
        numeros = numeros[:14]
    if len(numeros) <= 11:
        return formatar_cpf(numeros)
    else:
        return formatar_cnpj(numeros)

def formatar_cpf(cpf):
    cpf1 = ''.join(filter(str.isdigit, cpf))
    if len(cpf1) <= 3:
        return cpf1
    elif len(cpf1) <= 6:
        return f"{cpf1[:3]}.{cpf1[3:]}"
    elif len(cpf1) <= 9:
        return f"{cpf1[:3]}.{cpf1[3:6]}.{cpf1[6:]}"
    else:
        return f"{cpf1[:3]}.{cpf1[3:6]}.{cpf1[6:9]}-{cpf1[9:11]}"

def formatar_cnpj(numero_cnpj):
    cnpj = ''.join(filter(str.isdigit, numero_cnpj))
    if len(cnpj) <= 2:
        return cnpj
    elif len(cnpj) <= 5:
        return f"{cnpj[:2]}.{cnpj[2:]}"
    elif len(cnpj) <= 8:
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:]}"
    elif len(cnpj) <= 12:
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:]}"
    else:
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
     
def remover_mascara(texto):
    return ''.join(filter(str.isdigit, texto))

def formatar_moeda(valor):
    if valor is None:
        valor = 0
    valor_str = f"{valor:,.2f}"
    valor_str = valor_str.replace(',', 'X').replace('.', ',').replace('X', '.')
    return f"R$ {valor_str}"

def converter_float(texto_moeda):
    if not texto_moeda:
        return 0.0
    texto = texto_moeda.replace('R$', '').replace(' ', '').strip()
    if ',' in texto:
        texto = texto.replace('.', '').replace(',', '.')
    return float(texto)

#def mascara_preco(valor):

def validar_telefone(telefone):
    if not telefone:
        return True
    else:
        numeros = ''.join(filter(str.isdigit, telefone))
        return len(numeros) in [10,11]

def mascara_telefone(texto):
    numeros = ''.join(filter(str.isdigit, texto))
    if len(numeros) > 11:
        numeros = numeros[:11] 
    if len(numeros) == 0:
        return ''
    elif len(numeros) <= 2:
        return f"({numeros}"
    elif len(numeros) <= 6:
        return f"({numeros[:2]}) {numeros[2:]}"
    elif len(numeros) <= 10:
        return f"({numeros[:2]}) {numeros[2:6]}-{numeros[6:]}"
    else:
        return f"({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}"

def validar_cep(cep):
    if not cep:
        return True
    else:
        numeros = ''.join(filter(str.isdigit, cep))
        return len(numeros) == 8

def mascara_cep(texto):
    numeros = ''.join(filter(str.isdigit, texto))
    if len(numeros) > 8:
        numeros = numeros[:8] 
    if len(numeros) == 0:
        return ''
    elif len(numeros) <= 5:
        return numeros
    else:
        return f"{numeros[:5]}-{numeros[5:]}"

def mascara_moeda(texto):
    numeros = ''.join(filter(str.isdigit, texto))
    if not numeros:
        return 'R$ 0,00'
    valor_centavos = int(numeros)
    reais = valor_centavos // 100
    centavos = valor_centavos % 100
    reais_str = f"{reais:,}".replace(',', '.')
    return f"R$ {reais_str},{centavos:02d}"

def converter_status(status_bool):
    return "Ativo" if status_bool else "Inativo"

