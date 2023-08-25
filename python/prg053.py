frase = int(input('Digite um frase: '))

if frase == frase[::-1]:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')