import random

aluno1 = input('Digite o 1º aluno: ')
aluno2 = input('Digite o 2º aluno: ')
aluno3 = input('Digite o 3º aluno: ')
aluno4 = input('Digite o 4º aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi:', random.choice(alunos))