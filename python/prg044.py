preço = float(input('Coloque o preço do produto: '))
opção = int(input('''Agora, ESCOLHA A FORMA DE PAGAMENTO:
    [1] - à vista dinheiro/cheque
    [2] - à vista no cartão
    [3] - em até 2x no cartão
    [4] - 3x ou mais no cartão  '''))

if opção == 1:
    print(f'O produto de R${preço} com desconto de 10% agora custa {preço - (preço * 0.10)} ')
elif opção == 2:
    print(f'O produto de R${preço} com desconto de 5% agora custa {preço - (preço * 0.05)}')
elif opção == 3:
    print(f'O produto de R${preço} será parcelado em 2x e sem desconto. Duas parcelas de {(preço / 2):.2f}')
elif opção == 4:
    print(f'O produto de R${preço} aerá parcelado com desconto de 20%. 3 parcelas de {(preço - (preço * 0.20)) / 3:.2f}')