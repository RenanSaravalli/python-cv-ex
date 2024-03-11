''' Lê dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
O programa deverá realizar a operação solicitada em cada caso
'''
from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
        sleep(1)
        print('''--MENU DE OPERAÇÕES--
[1]Somar
[2]Multiplicar
[3]Número maior
[4]Novos números
[5]Sair do programa
''','=-'*10)
        opcao = int(input('Qual opção: '))
        if opcao == 1:
            print('{} + {} = {}'.format(n1,n2,n1+n2))
        elif opcao == 2:
            print('{} x {} = {}'.format(n1,n2,n1*n2))
        elif opcao == 3:
            if n1 > n2:
                print('{} > {}'.format(n1,n2))
            elif n1 == n2:
                print('{} = {}'.format(n1,n2))
            else:
                print('{} > {}'.format(n2,n1))
        elif opcao == 4:
            n1 = int(input('Digite um novo valor: '))
            n2 = int(input('Digite o segundo novo valor: '))  
        elif opcao == 5:
             print('Finalizando....')
             sleep(1)
        else:
             print('Opção inválida, tente novamente!!')    
        print('=-='*10)
print('ADEUS!')
           
    
