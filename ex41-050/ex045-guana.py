#jokenpô de outro modo
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Escolha sua jogada!! 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tespura''')
jogador = int(input('Qual você escolhe? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('=-' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 10)

if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE!!')
    elif jogador == 1:
        print('HUMANO VENCE!!')
    elif jogador == 2:
        print('MÁQUINA VENCE!!')
    else:
        print('JOGADA DO HUMANO INVÁLIDA, ESCOLHA UMA DAS OPÇÕES ACIMA!!')
elif computador == 1: #papel
    if jogador == 0:
        print('MÁQUINA VENCE!!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('HUMANO VENCE!!')
    else:
        print('JOGADA DO HUMANO INVÁLIDA, ESCOLHA UMA DAS OPÇÕES ACIMA!!')
elif computador == 2: #tesoura
    if jogador == 1:
        print('MÁQUINA VENCE!!')
    elif jogador == 0:
        print('HUMANO VENCE!!')
    elif jogador == 2:
        print('EMPATE!!')
    else:
        print('JOGADA DO HUMANO INVÁLIDA, ESCOLHA UMA DAS OPÇÕES ACIMA!!')
