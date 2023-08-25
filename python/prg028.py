import random 
num = random.randint(0,5)

usu = int(input('Digite um número inteiro de 0 à 5: '))

if usu == num: 
    print('Você acertou o número escolhido!.')
else:
    print('Sinto muito, você errou :( ')