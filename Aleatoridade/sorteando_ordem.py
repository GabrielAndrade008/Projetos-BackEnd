print('Sistema de escolha de grupos aleatoriamente para apresentação')
print('='*40)

import random

aluno1= str(input('Aluno 1: '))
aluno2= str(input('Aluno 2: '))
aluno3= str(input('Aluno 3: '))
aluno4= str(input('Aluno 4: '))

lista_grupos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_grupos)

print(f'A ordem para apresentação do trabalho é:')
print(lista_grupos)
