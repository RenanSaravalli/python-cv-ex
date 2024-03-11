# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(*num):
    print('=-'*20)
    print('Analisando os valores passados...')
    if num == ():
        print('Nenhum valor informado!')
    else:
        for v in num:
            print(f'{v}', end=' ', flush=True)
            sleep(0.3)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    
            
maior(2, 9, 4, 5, 7, 5, 6, 5)

maior(1,2)

maior(0)

maior()