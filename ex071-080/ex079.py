#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = [] 

while True:
    add = int(input('Digite um valor: '))
    if add in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(add)
    resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp in 'Nn':
        break
print('-='*20)
valores.sort()
print(f'Você digitou os valores {valores}')
        
