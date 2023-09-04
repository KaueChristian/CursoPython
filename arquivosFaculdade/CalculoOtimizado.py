import random
import sympy as sp

# Converte uma string em uma lista de bases de números com ponto flutuante.
def convert(corda):
    chars = list(str(corda))
    num = list(map(ord, chars))
    bases = [sp.sqrt((b + 3**0.5)**2) for b in num]
    return bases

# Gera uma chave aleatória.
def gerar_chave():
    return random.random()

# Valida uma string, verificando se ela contém apenas caracteres alfanuméricos.
def validar_string(string):
    for c in string:
        if not c.isalnum():
            raise ValueError("A string só pode conter caracteres alfanuméricos.")

# Descriptografa uma lista de números com ponto flutuante, usando as bases fornecidas.
def desencriptar(entrada, bases):
    resultado = []
    for i in entrada:
        calculo = 0
        algarismos = list(str(i))
        for indice, digito in enumerate(algarismos[::-1]):
            calculo += int(digito)*(bases[indice]**indice)
        resultado.append(calculo)
    return resultado
