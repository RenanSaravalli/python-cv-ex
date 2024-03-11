#Lê vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
n = soma  = quant = 0
num = int(input('Digite um número inteiro [999] Para parar: '))
while num != 999:
    quant += 1
    soma += num
    num = int(input('Digite um número inteiro [999] Para parar: '))
print('{} foi a quantidade de números digitados e a soma entre eles é {}'.format(quant,soma))
