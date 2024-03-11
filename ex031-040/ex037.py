#Leia um número inteiro e peça para o usuário escollher qual será a base de conversão
num = int(input('Qual número você escolhe? '))
base = int(input('Para escolher a base de sua conversão digite 1 para binário, 2 para octal, 3 para hexadecimal. '))

if base == 1:
    print('{} Convertido para binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} Convertido para octal é {}'.format(num, oct(num)[2:]))
elif base == 3: 
    print('{} Convertido para hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('Escolha  1, 2 e 3!')
    