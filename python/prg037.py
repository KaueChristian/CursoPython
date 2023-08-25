print('='*10, 'Convertor binário', '='*10)

numero = int(input('Digite um número inteiro: '))

print('''[1] - Conversão bínaria.
[2] - Conversão octal.
[3] - Conversão hexadecimal''')
4
opcao = int(input('Selecione uma das opções: '))

if opcao == 1:
    print(f'{numero} em binário é: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} em octal é {oct(numero)[2:]}')
elif opcao == 3: 
    print(f'{numero} em Hexadecimal é {hex(numero)[2:]}')
else: 
    print(f'{opcao} não é uma opção válida.')
