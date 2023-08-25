print('='*20, 'Comparador', '='*20)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior')
elif num1 == num2:
    print('Os valores inseridos são iguais')
else:
    print('Error.')