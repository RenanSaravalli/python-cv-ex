print('='*20)
print('{:^20}'.format('BANCO RS'))
print('='*20)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totalCed = 0

while True:
    if total >= ced:
        total -= ced
        totalCed += 1
    else:
        print(f'Total de {totalCed} de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        else:
            ced = 1
    
        if total == 0:
            break