#Verifica se um número é ímpar ou par
num = int(input('Digite um número inteiro: '))
if num%2 == 0:
    print('Seu número {} é PAR!'.format(num))
else:
    print('Seu número {} é ÍMPAR!'.format(num))