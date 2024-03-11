#Calcula hipotenusa

import math
co = float(input('Digite o cateto oposto de seu Triângulo retângulo: '))
ca = float(input('Digite o cateto adjacente de seu Triângulo retângulo:'))

hipo = math.sqrt(co*co + ca*ca)
print('A hipotenusa de seu triângulo retângulo é equivalente á {:.2f}'.format(hipo))
