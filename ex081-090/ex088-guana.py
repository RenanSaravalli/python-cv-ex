from random import randint 
from time import sleep
mega = []
sena = []
cont = 0
print('-'*20)
print('{:^20}'.format('JOGA NA MEGA SENA'))
print('-'*20)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
print('-='*5, f'SORTEANDO {jogos} JOGOS', '-='*5)
while total <= jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in mega:
            mega.append(num)
            cont +=1 
        if cont >= 6:
            break
    total += 1
    mega.sort()
    sena.append(mega[:])
    mega.clear()

for i, n in enumerate(sena):
    sleep(1)
    print(f'Jogo {i+1}: {n}')
print('-='*5,'< BOA SORTE! >', '-='*5)
    