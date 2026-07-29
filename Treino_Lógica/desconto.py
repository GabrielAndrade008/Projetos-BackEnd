preço_produto = float(input('Digite o valor do produto: '))
print('Você tem direito a 10% de desconto')

desconto = preço_produto *0.1
novo_preço = preço_produto - desconto

print(f'Aplicando o desconto, o novo preço será R${novo_preço}')