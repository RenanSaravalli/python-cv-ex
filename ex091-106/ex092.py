#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos vai se aposentar.
from datetime import datetime
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - idade
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa['ctps'] == 0:
    print('=-'*30)
    print(pessoa)
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
else:
    
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário R$ '))

    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)

    print('=-'*30)
    print(pessoa)
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')