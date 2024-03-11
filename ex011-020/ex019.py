#Sorteia aluno

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista_alunos = [a1, a2, a3, a4]
print('O aluno que vai apagar o quadro é o {}'.format(random.choice(lista_alunos)))
