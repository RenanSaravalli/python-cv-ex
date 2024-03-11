#Simula o funcuonamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*20)
print('{:^20}'.format('BANCO RS'))
print('='*20)
ced50 = ced20 = ced10 = ced1 = 0

valor = int(input('Que valor você quer sacar? R$'))
while True:
    while valor >= 50:
        ced50 += 1 
        valor -= 50
    
    while valor >=20:
        ced20 += 1
        valor -= 20

    while valor >= 10:
         ced10 += 1
         valor -= 10

    while valor >= 1:
         ced1 += 1
         valor -= 1

    if valor == 0:
            break

print(f'Total de {ced50} cédulas de R$50')
print(f'Total de {ced20} cédulas de R$20')
print(f'Total de {ced10} cédulas de R$10')
print(f'Total de {ced1} cédulas de R$1')
print('='*20)
print('Volte sempre ao BANCO RS! Tenha um bom dia!')