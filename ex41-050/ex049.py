#Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for

num = int(input('Digite um número:'))
print('A tabuada do número {} é:'.format(num))
for c in range(0, 11):
    mult = num * c
    print('{} x {} : {}'.format(num, c, mult))