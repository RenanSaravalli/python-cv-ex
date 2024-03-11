# Melhorando o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-='*10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
primeiro = t
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print('{}'.format(primeiro), '-> ', end='')
        c += 1
        primeiro+= r 
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Sua Progressão Aritmética foi finalizada com {} termos!'.format(total))
    

        
