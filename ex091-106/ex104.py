#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python, só que fazendo a validação para aceitar apenas um valor numérico. Ex n = leiaInt('Digite um n')
def leiaInt(n):
    while True:
        v = str(input(n))
        if v.isnumeric():
            n = int(v)
            return n
        else:
            print('ERRO! Digite um número inteiro válido.')
             

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
