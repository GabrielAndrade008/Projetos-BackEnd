numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:  #O numero digitado é dividido por 2 e seu resto vai determinar se é par ou impar. Será par se o resto for 0.
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')