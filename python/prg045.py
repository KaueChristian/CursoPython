import random

escolha = input('Escolha Pedra, Papel ou Tesoura: ').lower()

while escolha not in ['pedra', 'papel', 'tesoura']:
    escolha = input('Escolha inválida. Escolha Pedra, Papel ou Tesoura')

ComputadorEscolha = random.choice(['pedra', 'papel', 'tesoura'])

if escolha == ComputadorEscolha:
    print('Empate!')
elif escolha == 'pedra':
    print('Você ganhou!') if ComputadorEscolha == 'tesoura' else print('Você perdeu!')
elif escolha == 'papel':
    print('Você ganhou!') if ComputadorEscolha == 'pedra' else print('Você perdeu!')
elif escolha == 'tesoura':
    print('Você venceu!') if ComputadorEscolha == 'papel' else print('Você perdeu!')