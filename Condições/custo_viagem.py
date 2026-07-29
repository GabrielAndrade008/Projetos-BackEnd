distancia = float(input('Qual é a distância da sua viagem em KM?: '))
print(f'Em breve você começará uma viagem de {distancia} Km.')

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'O preço da sua passagem será de R${preço:.2f}')