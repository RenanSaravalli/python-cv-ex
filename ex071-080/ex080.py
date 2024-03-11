#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.
valores = []
for c in range(0,5):
    add = int(input('Digite um valor: '))
    if c == 0:
        print('Adicionado ao final da lista...')
        maior = add
        menor = add
        valores.append(add)
    else:
        if add > maior:
            print('Adicionado ao final da lista...')
            maior = add
            valores.append(add)
        if add < menor:
            print('Adicionado na posição 0 da lista...')
            menor = add
            valores.insert(0,add)
        if add > menor and add < maior:
            print('Adicionado na posição 1 da lista...')
            valores.insert(1,add)
print('-='*20)
print(f'Os valores digitados em ordem foram {valores}')