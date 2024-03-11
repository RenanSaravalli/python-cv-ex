#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior. 
from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(1,6):
        n = randint(1,10)
        lista.append(n)
        print(n, end=' ',flush=True)
        sleep(0.4)
    print('PRONTO!')


def somaPar(lista):
    somaTot = 0
    for v in lista:
        if v % 2 == 0:
            somaTot += v
    print(f'Somando os valores pares de {lista}, temos {somaTot}')

numeros = []
sorteia(numeros)
somaPar(numeros)