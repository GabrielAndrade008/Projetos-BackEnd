km = float(input('Quantos KM rodados?: '))
dias = int(input('Quantos dias alugados?: '))

pago = (dias * 60) + (km * 0.15) 
print(f'O total a pagar é de {pago:.2f}')