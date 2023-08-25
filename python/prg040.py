print('='*20, 'Calculadora de Média', '=')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2

if média < 5:
    print('[REPROVADO]')
elif média > 5 and média < 6.9:
    print('[recuperação]')
elif média > 7:
    print(['APROVADO'])