# Jogo Par ou ímpar com o computador. O jogo só sera interrompido quando o jogador PERDER, mostrando  o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
c = 0


while True:
    comput = randint(1,10)
    num = int(input('Diga um valor: '))
    quest = input('Par ou Ímpar? [P/I] ').upper().strip()
    print('-'*20)

    resultado = num + comput

    if resultado % 2 == 0:
        confResult = 'P'
    else:
        confResult = 'I'

    if quest == 'P':
        questComp = 'I'
    else:
        questComp = 'P'

    
    print(f'Você jogou {num} e o computador {comput}. Total de {resultado} DEU ''PAR' if resultado%2==0  else 'ÍMPAR')
    print('-'*20)

    if quest == confResult:
        print('Você VENCEU!')
        print('Vamos jogar novamente ...')
        print('=-'*20)
        c +=1
    else:
        print('você PERDEU!')
        print('=-'*20)
        print(f'GAME OVER! Você venceu {c} vezes.')
        break
        
