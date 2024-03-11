#lê vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = 'S'
media = 0
divisor = 0
while cont == 'S':
    num = int(input('Digite um número: '))
    cont = (input('Digite [S] para continuar. Digite [N] para parar: ')).upper().strip()
    divisor += 1
    media += num
    if divisor == 1:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
media = media / divisor
print('Você digitou {} números e a média foi: {:.2f}'.format(divisor, media))
print('O maior número foi o {} e o menor foi o {}'.format(maior, menor))
    