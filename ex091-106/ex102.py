# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial. 
def fatorial(n, show = False):
    f = 1
    for c in range(n, 0, -1):
        f*=c
        if show == True:
            print(f'{c}',end='')
            print(' x 'if c > 1 else ' = ', end='')
                 
    return f 

print('-'*30)
print(fatorial(5,show = True))

