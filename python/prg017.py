from math import hypot

cateto1 = float(input('Digite o cateto oposto: '))
cateto2 = float(input('Digite o cateto adjascente: '))
hipot = hypot(cateto1, cateto2)
 
print(f'A hipotenusa dos catetos {cateto2} e {cateto1} é {hipot:.1f}')