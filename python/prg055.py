ListaPeso = []

for c in range(0, 5):
    peso = int(input('Digite o seu peso em KGs: '))
    ListaPeso.append(peso)

ListaPeso.sort()
print(f'O maior peso entre os digitados é: {ListaPeso[4]}KGs')
print(f'O menor peso digitado é: {ListaPeso[0]}KGs')