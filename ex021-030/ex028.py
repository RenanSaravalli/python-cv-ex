#Computador sorteia um número de 0 a 5 e peça para o usúario tentar descobrir qual foi o número escolhido pelo computador.
import random
num = random.randint(0,5)
print(num)
tent = int(input('Chute um número entre 0 a 5: '))
if tent == num:
    print('ACERTOU!!!')
else:
    print('ERROU!!')