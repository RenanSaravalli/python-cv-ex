#Faça um programa que ajude um jogador da MEGA SENA  a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint 
from time import sleep
sena = []

print('-'*20)
print('{:^20}'.format('JOGA NA MEGA SENA'))
print('-'*20)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, f'SORTEANDO {jogos} JOGOS', '-='*5)
for j in range(0,jogos):
    for num in range(0,6):
        sorteio = randint(1,60)
        if sorteio not in sena: 
            sena.append(sorteio)
    sena.sort()
    sleep(1)
    print(f'Jogo {j+1}: {sena}')
    sena.clear()
sleep(1)
print('-='*5,'< BOA SORTE! >', '-='*5)