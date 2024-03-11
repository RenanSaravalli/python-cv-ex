#Pedra, papel e tesoura
import random
jogador = input('ESCOLHA: PEDRA, PAPEL OU TESOURA. ')
comp = ['PEDRA', 'TESOURA', 'PAPEL']
aleat = random.choice(comp)
print('Eu escolho: {}'.format(aleat))
if jogador == 'TESOURA' and aleat == 'TESOURA':
    print('EMPATE')
elif jogador == 'TESOURA' and aleat == 'PEDRA':
    print('GANHEI! CHUPA HUMANO')
elif jogador == 'TESOURA' and aleat == 'PAPEL':
    print('PERDI, DROGA!')

if jogador == 'PEDRA' and aleat == 'PEDRA':
    print('EMPATE')
elif jogador == 'PEDRA' and aleat == 'PAPEL':
    print('GANHEI! CHUPA HUMANO')
elif jogador == 'PEDRA' and aleat == 'TESOURA':
    print('PERDI, DROGA!')

if jogador == 'PAPEL' and aleat == 'PAPEL':
    print('EMPATE')
elif jogador == 'PAPEL' and aleat == 'TESOURA':
    print('GANHEI! CHUPA HUMANO')
elif jogador == 'PAPEL' and aleat == 'PEDRA':
    print('PERDI, DROGA!')