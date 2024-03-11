'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. escreva('Olá mundo!')
---------
olá mundo!
----------
'''

def texto(txt):
    tam = len(txt) + 4
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)


text = input('Escreve ai! ')

texto(text)

texto('Opa, Bom dia !')