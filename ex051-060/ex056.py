#Lê o nome, idade e sexo de 4 pessoas. no final do programa, mostre: A média de idade do grupo. Qual é o nome do homem mais velho. Quantas mulheres tem menos de 20 anos 
medidade = 0
velho = 0
idade = 0
nom = ''
mulher = 0
for c in range(1, 5):
    print('-'*5, '{}ªPessoa'.format(c),'-'*5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    medidade += idade
    if c == 1 and sexo == 'M':
        velho = idade
        nom = nome
    else:
        if velho < idade and sexo == 'M':
            velho = idade
            nom = nome
    if sexo == 'F' and idade < 20:
        mulher += 1

medidade = medidade / 5
print('A média de idade do grupo é de {}'.format(medidade))
print('O nome do homem mais velho é {} que possui idade {}'.format(nom, velho))   
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
