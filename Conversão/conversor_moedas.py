print('='*40)
print('Bem-vindo ao conversor de moedas! (Conversão de Real para Dólar e Euro)')
print('='*40)
real_brasileiro = float(input('Digite quantos reais você tem na carteira: R$ '))

dolar = real_brasileiro/4.98
euro = real_brasileiro/5.89

print(f'Com R$ {real_brasileiro:.2f} você pode comprar US$ {dolar:.2f} ou €{euro:.2f}') 