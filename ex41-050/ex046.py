#Mostra na tela uma contagem regressiva para o estoura de fogos de artifício indo de 10 até 0, com uma pausa de 1 segundo entre eles
from time import sleep
print('Vamo soltar os fogos de Artifício em ')
for c in range (10, -1, -1):
    print(c)
    sleep(1)
    if c == 0:
        print('BUUUUMMM')
    