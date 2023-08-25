from datetime import date

atual = date.today().year
Nascimento = int(input('Data de Nascimeno: '))
idade = atual - Nascimento

if idade <= 9:
    print('Você está na Turma MIRIM. ')
elif idade > 9 and idade <= 14:
    print('Você está na Turma INANTIL. ')
elif idade > 14 and idade <= 19:
    print('Você está na turna JÙNIOR. ')
elif idade > 19 and idade <= 25:
    print('Você está na turma SÊNIOR. ')
elif idade > 25:
    print('Você está na turma MASTER. ')