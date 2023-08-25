frase = str(input('Digite uma frase: ')).lower()
print(f"A letra A aparece{frase.count('a')}")
print(f"A primeira letra A aparece em {frase.find('A') + 1}")
print(f"A última letra A aparece em {frase.rfind('A') + 1}")
