#Lê um número inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de fibonacci 
print('-'*40)
print('Sequência de Fibonacci')
print('-'*40)
t = int(input('Quantos termos você quer mostrar? '))
print('~'*40)
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2),'-> ', end='')
t1 += t2
print('{}'.format(t1),'-> ', end='')
c = 3
while c <= 10:
    t3 = t1 + t2
    print('{}'.format(t3),'-> ',end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')