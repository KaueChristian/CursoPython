somátorio = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        somátorio += numero

print(f'a soma entre os números múltiplos de 3 é {somátorio}')
