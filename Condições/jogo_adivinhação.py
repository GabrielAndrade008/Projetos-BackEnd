from random import randint #Importa o randint da biblioteca random
from time import sleep #Faz o computador "dormir" por uns segundos
computador = randint(0,5) #Faz o computador sortear entre 0 e 5
print('='*40)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('='*40)
jogador = int(input('Em que número pensei?: ')) #Usuário vai digitar o número pra tentar adivinhar
print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS, você venceu!')
else:
    print(f'GANHEI, eu pensei no número {computador} e não no {jogador}')
