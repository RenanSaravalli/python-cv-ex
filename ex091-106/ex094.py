#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade do grupo. C) Uma lista com todas as mulheres D) Uma lista com todas as pessoas com idade acima da média
pessoa = {}
grupo = []
media = soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())

    pessoa.clear()

    while True:
        resp = input('Quer continuar [S/N] ').upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp in 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoas cadastradas.')

media = soma / len(grupo)
print(f'- A média de idade é de {media:5.2f} anos.')

print('- As mulheres cadastradas foram: ', end=' ')
for c in grupo:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')

print('\n- Lista das pessoas que estão com idade acima da média: ')
print()
for p in grupo:
    if p['idade'] > media:
        for k ,v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
        print()
print('<< ENCERRADO >>')