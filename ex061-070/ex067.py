#Mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
cont = 0
n = int(input('Quer ver a tabuada de qual valor? (valor negativo se quiser parar) '))
print('-'*20)
while True:
    cont += 1
    print(f'{n} x {cont} = {n*cont}')
    if cont >= 10:
        print('-'*20)
        n = int(input('Quer ver a tabuada de qual valor? (valor negativo se quiser parar) '))
        print('-'*20)
        cont = 0
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!!')