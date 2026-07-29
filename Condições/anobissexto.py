print('Calculador de ano bissexto - Vamos verificar se o ano digitado foi ou será bissexto!')
print('='*40)

ano = int(input('Digite um ano do calendário: '))
print('='*40)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É bissexto.')
else:
    print(f'O ano {ano} NÃO é bissexto.')