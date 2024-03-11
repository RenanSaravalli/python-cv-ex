#Lê o ano de nascimento de sete pessoas. No final mostre quantas pessoas não atingiram a maioridade e quantas já são maiores.
maiores = 0
menores = 0
ano = 2024
for c in range (1, 8):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano - nasc
    if idade > 18:
        maiores += 1
    else:
        menores +=1
print('A quantidade de pessoas maiores de idade é {}'.format(maiores))
print('A quantidade de pessoas menores de idade é {}'.format(menores))     
