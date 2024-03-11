#Lê a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá  perguntar se o usuário que ou não continuar. No final, mostre: A) Quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados. C) Quantas mulheres tem menos de 20 anos.
maiorIdade =  homens =  mulher = 0


while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('Idade: '))
    while idade < 0 and idade not in int:
        idade = int(input('Idade: '))

    if idade > 18:
        maiorIdade += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip() [0] #[0]-Serve para pegar a primeira letra
    
    if sexo == 'M':
        homens += 1

    if idade < 20 and sexo == 'F':
        mulher +=1
    
    print('-'*20)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
    
    if resp == 'N':
        break
print('='*5, 'FIM DO PROGRAMA', '-'*5)

print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')
print(f'Ao todo temos {homens} homens cadastrados')
if mulher == 1:
    print(f'E temos {mulher} mulher com menos de 20 anos')
else:
    print(f'E temos {mulher} mulheres com menos de 20 anos')



    