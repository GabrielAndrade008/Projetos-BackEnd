velocidade_carro = float(input('Qual a velocidade atual do carro?: '))
multa = (velocidade_carro - 80) * 7

if velocidade_carro <=80:
    print('Tenha um bom dia, dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite de velocidade permitido, que é de 80km/h') 
    print(f'Você deve pagar uma multa de R${multa}')