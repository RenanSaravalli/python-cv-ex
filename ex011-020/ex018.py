#Transforma ângulo

import math
ang = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno do ângulo é {:.2f}, o cosseno {:.2f}, e a tangente {:.2f}.'.format(sen,cos,tan))