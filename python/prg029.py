velocidade = float(input('Qual a velocidade do carro?: '))
if velocidade > 80:
    print(f'Aa multa a ser paga custa R${(velocidade - 80) * 7}')
else:
    print('Está na velocidade permitida.')