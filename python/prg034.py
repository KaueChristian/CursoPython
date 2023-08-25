salario = float(input('Digite o seu salário: '))
if salario > 1250:
    print(f'O seu salário teve um aumento de 10%, seu salário atual é R${salario + (salario * 0.10):.2f}')
else:
    print(f'O seu salário teve um aumento de 15%, seu salário atual é R${salario + (salario * 0.15):.2f}')
