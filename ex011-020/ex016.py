#Tranforma número float para int

from math import trunc
num = float(input('Digite um número: '))
n = trunc(num)
print('O valor digitado foi {} e sua porção inteira é {}'.format(num,n))
