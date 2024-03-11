#Lê número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        total += 1
if total == 2:
    print('O número {} foi divisível {} vezes então:'.format(num,total), end=' ')
    print('O número {} é um número primo!'.format(num))
else:
     print('O número {} foi divisível {} vezes então:'.format(num,total), end=' ')
     print('O número {} não é um número primo!'.format(num))
    
    
    