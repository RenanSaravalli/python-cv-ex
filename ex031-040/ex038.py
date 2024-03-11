#Lê dois nº inteiros e compare-os mostrando na tela a mensagem: -O primeiro valor é maior, o segundo valor é maior, não existe valor maior os dois são iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

if n1 > n2:
    print('O primeiro número {} é maior que o segundo número {}'.format(n1,n2))
elif n2 > n1:
    print('O segundo número {} é maior que o primeiro número {}'.format(n2,n1))
else:
    print('Não existe número maior, os dois são iguais!')