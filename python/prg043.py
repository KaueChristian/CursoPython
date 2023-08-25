peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)

print(f'Seu IMC é {imc:.2f}. Você está ', end="")

if imc < 18.5:
    print('Abaixo do peso.')
elif imc == 18.5 and imc < 25:
    print(' No peso ideal.')
elif imc == 25 and imc < 30:
    print('Com sobrepeso.')
elif imc == 30 and imc < 40:
    print('Com Obesidade.')
elif imc > 40:
    print('Com obesidade mórbida.')