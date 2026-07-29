print('Você tem direito a um desconto de 5%')

preco=float(input("Digite o preço do produto: "))
desconto = preco - (preco * 5/100)
print('====================================================')

print(f'O desconto é de R$ {desconto:.2f}')