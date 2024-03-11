#Lê o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: até 9anos:MIRIM, até 14 anos: INFANTIL, Até 19 anos: JUNIOR, Até 20 anos SÊNIOR, Acima: MASTER
ano = int(input('Qual seu ano de nascimento? '))
atualAno = 2024
idade = atualAno - ano

if idade <= 9:
    print('Com sua idade {} anos, sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Com sua idade {} anos, sua categoria é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Com sua idade {} anos, sua categoria é JUNIOR!'.format(idade))
elif idade <= 20:
    print('Com sua idade {} anos, sua categoria é SÊNIOR!'.format(idade))
else:
    print('Com sua idade {} anos, sua categoria é MASTER!'.format(idade))