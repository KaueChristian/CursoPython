from datetime import date

atual = date.today().year
DataNascimento = input('Digite seu ano de nascimento: ')
idade = atual - DataNascimento

if idade == 18:
    print('Você deve se alistar obrigatoriamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Falta {saldo} anos para voce se alistar')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado à {saldo} anos')