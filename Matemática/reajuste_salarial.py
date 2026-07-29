salario = float(input("Digite o salário do funcionário: "))
print('Este funcionário tem direito a um reajuste salarial de 15%')
print('='*40)
reajuste = salario * 0.15
novo_salario = salario + reajuste

print(f"O valor do reajuste é: R$ {novo_salario:.2f}")