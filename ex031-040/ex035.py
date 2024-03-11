#Lê 3 retas e diga ao usuário se ele pode ou não formar um triângulo
r1 = float(input('Digite a primeira reta de seu Triângulo: '))
r2 = float(input('Digite a segunda reta de seu Triângulo: '))
r3 = float(input('Digite a terceira reta de seu Triângulo: ')) 
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Com essas retas você pode formar um triângulo.')
else:
    print('Com essas retas você não consegue formar um triângulo.')