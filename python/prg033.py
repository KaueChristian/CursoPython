num = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('digite mais um número: '))

menor = num
if num2 < num and num2 < num3:
    print(f'O menor número é {num2}')
elif num3 < num2 and num3<num:
    print(f'O menor número é {num3}')
else:
    print(f'O menor número é {num}')

maior = num
if num2 > num and num2 > num3: 
    print(f'O maior número é {num2}')
elif num3 > num2 and num3 > num:
    print(f'O maior número é {num3}')
else:
    print(f'O maior número é {num}')