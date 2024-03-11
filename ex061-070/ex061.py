#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
print('Gerador de PA')
print('-='*10)
t = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão da Progressão Aritmética desse termo: '))
c = 1
primeiro = t
while c <= 10:
    print('{}'.format(primeiro),'->',end=' ')
    c += 1
    primeiro += r
print('FIM')  