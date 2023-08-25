dia = int(input('Quantos dias alugados: '))
km = float(input('Quantos kms rodados: '))

print(f'O valor a pagar pelos dias e kms rodados é: R${(dia * 60) + (km * 0.15):.2f} ')