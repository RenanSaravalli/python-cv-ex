#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número.
from random import randint
from time import sleep
from operator import itemgetter
jog = {}
ranking = []
print('Valores sorteados: ')
for c in range(1,5):
    jog[f'jogador{c}'] = randint(1,6)
for k, v in jog.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jog.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('**RANKING DOS JOGADORES**')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar {v[0]} com {v[1]} no dado')
    sleep(1)