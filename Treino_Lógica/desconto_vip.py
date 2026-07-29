valor_compra = float(input('Digite o valor da sua compra no total: '))
cliente_vip = str(input('Você é cliente VIP? (S/N): ')).upper()

Vip = valor_compra * 0.2
desconto_vip = valor_compra - Vip

Nao_vip = valor_compra * 0.1
desconto_naovip = valor_compra - Nao_vip

print('='*40)

if cliente_vip == 'S':
    print('Por você ser cliente Vip, terá um desconto de 20%!')
    print(f'Sua compra foi de R${valor_compra}. Agora com seu novo desconto é de: R${desconto_vip}')
else:
    print('Por você ser cliente comum, terá um desconto de 10%!')
    print(f'Sua compra foi de R${valor_compra}. Com 10% de desconto ficará R${desconto_naovip}')