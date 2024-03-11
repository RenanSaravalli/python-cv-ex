#Mesmo desafio dos triângulos acrescentando o recurso de mostrar que tipo de Triângulo será formado: Equilátero, Isósceles, Escaleno
r1 = float(input('Digite um segmeto de um triângulo: '))
r2 = float(input('Digite o segundo segmento de um triângulo: '))
r3 = float(input('Digite o terceiro segmento de um triângulo: '))

triangulo = r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2

if triangulo:
    print('Com esses segmentos pode-se formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1: 
        print('Escaleno!')
    else:
        print('Isósceles!')
else: 
    print('Não é um triângulo')