r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceerio segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os segmentos é possivel se formar um triângulo.')
else:
    print('Com os segmentos não é possivel formar um triângulo.')