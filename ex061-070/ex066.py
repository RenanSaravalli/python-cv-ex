#Lê vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles 

s = c = 0
while True:
    n = int(input('Digite um número [Digite 999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores foi {s}!')