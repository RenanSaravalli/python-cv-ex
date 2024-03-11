#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno. 
print('-'*20) 
print('Controle de terreno')

def area(a, b):
    print(f'A área de um terreno {a}x{b} é de {a*b:.1f}m².')

l = float(input('Largura (m):'))
c = float(input('Comprimento (m):'))
area(l,c)