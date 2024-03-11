#Lê o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$1000. C) Qual é o nome do produto mais barato.
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)

total = maior = barato = 0

while True:
    prod = input('Nome do Produto: ')
    preco = int(input('Preço: R$ '))

    barato += 1

    total += preco

    if preco > 1000:
        maior += 1

    if barato == 1:
        menorProd = prod
        menorPrec = preco

    if menorPrec > preco:
        menorPrec = preco
        menorProd = prod

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('-'*5, 'FIM DO PROGRAMA', '-'*5)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menorProd} custando R${menorPrec:.2f}')
