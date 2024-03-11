#Lê o primeiro termo e a razão de uma Progreção aritmética. No final mostre os 10 primeiros termos dessa progreção
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da Progressão Aritmética desse termo: '))
decimo = t + (10 - 1) * r
print('Os 10 primeiros termos são: ')
for c in range(t, decimo + r, r):
    print('{}'.format(c), end=' -> ')
print('ACABOU')