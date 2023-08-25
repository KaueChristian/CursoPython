print('-'*5, "Empréstimo bancário", '-'*5)

casa = float(input('Digite o preço da casa escolhida: R$'))
print('Analisando...\n')
salario = float(input('Agora, Digite o séu salário: R$'))
print('Analisando...\n')
anos = int(input('Por fim, em quantos anos pretende pagar?: '))
print('Analise concluída!\n')

ValorMínimo = (salario * 0.30)
PrestacaoMensal = casa / (anos * 12)

if PrestacaoMensal <= ValorMínimo:
    print('O empréstimo será feito de acordo com os cálculos realizados!\n')
    print(f'A prestação mensal será de {PrestacaoMensal} durante {anos * 12} meses.')
else:
    print(f'Após a análise, o Empréstimo foi negado, o valor maximo para ocorrer o empréstimo é {ValorMínimo}') 