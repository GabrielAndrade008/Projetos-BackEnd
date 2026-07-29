print('Seja bem-vindo ao calculador de IMC - Versão Brasileira')
print('='*40)

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / altura**2
print('='*40)
print(f'Seu IMC é de: {imc:.3f}')