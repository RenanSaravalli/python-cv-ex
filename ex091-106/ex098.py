#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: Início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: A) de 1 até 10, de 1 em 1. B) de 10 até 0, de 2 em 2. C) uma contagem personalizada.
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1
        
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' ',flush=True)
            sleep(0.5)
            c += p 
        print('FIM!')
    else:
        c = i
        while c >= f:
            print(f'{c}',end=' ', flush=True)
            sleep(0.5)
            c -= p
        print('FIM!')


contador(1,10,1)

contador(10, 0,2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini,fim,pas)