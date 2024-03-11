#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B)Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leve.
princ = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    princ.append(pessoa[:])
    pessoa.clear()
    
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break


print('-='*20)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')

print(f'O maior peso foi de {maior}kg. Peso de ',end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {menor}kg. Peso de ',end='')        
for p in princ:          
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
