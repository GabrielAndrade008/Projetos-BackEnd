print('Sistema de escolha de alunos aleatoriamente para apagar o quadro')
print('='*40)

import random

aluno1= str(input('Aluno 1: '))
aluno2= str(input('Aluno 2: '))
aluno3= str(input('Aluno 3: '))
aluno4= str(input('Aluno 4: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
sortear = random.choice(lista_alunos)

print(f'O aluno escolhido para apagar o quadro foi {sortear}')
