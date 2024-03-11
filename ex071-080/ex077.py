#Crie um programa que tenha uma tupla com várias palavras (Não usar acentos). Depois disso, você deve mostrar, para cada palavra quais são as suas vogais.
p = ('aprender', 'programar','linguagem')

for v in p:
    print(f'\nNa palavra {v.upper()} temos', end = ' ')
    for letra in v:
        if letra in 'aeiou':
            print(letra, end=' ')