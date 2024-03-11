#Lê o peso de cinco pessoas. no final mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual é o peso da {}ª pessoa? '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print('O maior peso registrado foi de {}kg'.format(maior))
print('O menor peso registrado foi de {}kg'.format(menor))
    

        