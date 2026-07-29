import math

cateto_oposto = int(input('Digite o valor do Cateto Oposto: '))
cateto_adjacente = int(input('Digite o valor do Cateto Adjacente: '))
print('='*40)
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa do Cateto Oposto ({cateto_oposto}) e do Cateto Adjacente ({cateto_adjacente}) é {hipotenusa}')