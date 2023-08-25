from time import sleep

MaiorIdade = 0
NomeVelho = ''
MediaIdade = 0
Somaidade = 0
Mulher20 = 0

for c in range(4):
    nome = input('Nome: ').strip()  
    idade = int(input('Idade: '))
    sexo = input('Homem ou Mulher?: ').lower()
    Somaidade += idade
    
    print('Adicionando dados...')
    sleep(1.5)
    print('\n')

    if c == 1 and sexo == 'homem':
        MaiorIdade = idade
        NomeVelho = nome
    if sexo == 'homem' and idade > MaiorIdade:
        MaiorIdade = idade
        NomeVelho = nome
    if sexo == 'mulher' and idade < 20:
        Mulher20 += 1
    
  
MediaIdade = (Somaidade / 4)
print(f'A média da idade dos integrantes é {Somaidade:.2f}')
print(f'O homem mais velho tem {MaiorIdade} e se chama {NomeVelho}') 
print(f'Ao todo, são {Mulher20} mulheres com menos de 20 anos')
