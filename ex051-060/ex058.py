#Melhorando o jogo do desafio028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
tentativas = 1
comput = randint(1,10)


print('-'*12,'JOGO DA ADVINHAÇÃO', '-'*12)
jogador = int(input('Adivinhe o número entre 1 a 10 que eu pensei: '))
if jogador == comput:
    print('ACERTOU DE PRIMEIRA')
else:
    while jogador != comput:
        if jogador != comput:
            tentativas +=1
            if jogador > comput:
                jogador = int(input('Menos... Tente novamente: '))
            elif jogador < comput:
                jogador = int(input('Mais... Tente novamente: '))
        
print('Finalmente ACERTOU, na {}ª tentativa'.format(tentativas))
                