valor = int(input('Digite um número e irei informar se está entre 10 e 20: '))
if valor <=10:
    print(f'O número {valor} NÃO está entre 10 e 20')
elif valor >10 and valor <=20:
    print(f'O número {valor} ESTÁ entre 10 e 20')
else:
    print('Erro, tente novamente.')