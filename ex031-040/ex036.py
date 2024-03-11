#Aprovador de empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, salário do comprador e em quantos anos ele vai pagar. 
Vcasa = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você planeja pagar a casa? '))

prestMensal = anos * 12 
NprestMensal =  Vcasa / prestMensal

if NprestMensal < 30 * sal / 100:
    print('Para pagar a casa de R${} em {} anos o valor da prestação será de R${:.2f}'.format(Vcasa, anos, NprestMensal))
    print('Empréstimo concedido!!')
elif NprestMensal > 30 * sal / 100:
    print('Para pagar a casa de R${} em {} anos o valor da prestação será de R${:.2f}'.format(Vcasa, anos, NprestMensal))
    print('EMPRÉSTIMO NEGADO!!')
