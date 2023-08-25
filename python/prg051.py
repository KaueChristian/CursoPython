PrimeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
décimo = PrimeiroTermo + (10 - 1) * razao
c = 0

for c in range(PrimeiroTermo, décimo + razao, razao):
    print(c, end=" ")