#Pergunta salário. Caso o salário seja superior a R$1250,00 aumente 10%. Se for inferior ou iguais aumente 15%
sal = int(input('Qual seu salário? '))
if sal > 1250:
    aumento1 = sal * 10 / 100
    print('Seu salário {:.2f} com o aumento de 10por cento fica {:.2f}'.format(sal, sal + aumento1))
else:
    aumento2 = sal * 15 /100
    print('Seu salário {:.2f} com o aumento de 15 por cento fica {:.2f}'.format(sal, sal + aumento2))