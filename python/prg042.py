lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado1 == lado2 and lado2 == lado3:
    print('Triângulo EQUILÁTERO. ')
elif lado1 == lado2 and lado2 == lado3 or lado1 == lado3:
    print('Triângulo ISÓSCELES. ')
else:
    print('Triângulo ESCALENO. ')