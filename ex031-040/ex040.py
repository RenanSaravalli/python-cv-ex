#Lê duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média: Média abaixo de 5.0: REPROVADO. Média entre 5.0 6.9: RECUPERAÇÃO. Média 7.0 ou superior: APROVADO
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Com media {} você foi REPROVADO!!'.format(media))
elif media <= 6.9:
    print('Com media {} você está de RECUPERAÇÃO!!'.format(media))
else:
    print('Com media {} você foi APROVADO!!'.format(media))