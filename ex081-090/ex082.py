#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas. 
valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-='*20)
print(f'A lista completa é {valores}')

for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')