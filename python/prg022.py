nome = str(input('Digite seu nome completo : ')).strip()
print(f'Seu nome em Maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras. ')