nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) /3

print(f'A média final foi {media}')

if media >= 7:
    print('Aluno aprovado!')
elif media >= 5 and 6.9:
    print('Aluno de recuperação')
else:
    print('Aluno reprovado')