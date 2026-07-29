salario_funcionario = float(input('Digite o salário atual do funcionário: '))

if salario_funcionario >=1251:
    aumento = salario_funcionario *0.1
    novo_salario = aumento + salario_funcionario
elif salario_funcionario <=1250:
    aumento = salario_funcionario *0.15
    novo_salario = aumento + salario_funcionario
else:
    print('Erro, tente novamente')

print(f'O novo salário do funcionário será: R${novo_salario}')