#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente 

alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    alunos.append([nome, [nota1,nota2], media])

    resp = input('Quer continuar [S/N]: ')
    if resp in 'Nn':
        break
print('-='*30)

print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i,n in enumerate(alunos):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8.1f}')
print('-'*26)
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno ? (999 INTERROMPE.)'))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('--VOLTE SEMPRE--')
    