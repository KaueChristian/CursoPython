from datetime import date

atual = date.today().year
lista = []
for c in range (0, 7):
    data = int(input('Digite o ano de Nascimento: '))
    idade = atual - data
    lista.append(idade)

maior_de_idade = 0
menor_de_idade = 0
for idade in lista:
    if idade >=18:
        maior_de_idade += 1
    else: 
        menor_de_idade += 1

print(f'As pessoas maiores de idade são: {maior_de_idade}')
print(f'As pessoas que não são maiores são: {menor_de_idade}')
