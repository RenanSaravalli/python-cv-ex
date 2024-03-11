#Sorteia ordem de alunos

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista_alunos = [a1,a2,a3,a4]
print('A ordem dos alunos que vão apresentar a atividade é: {}'.format(random.sample(lista_alunos, 4)))