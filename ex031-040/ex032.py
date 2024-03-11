#Verifica se um ano é bissexto
ano = int(input('Digite um ano: '))
if ano%4 == 0:
    print('O seu ano é BISSEXTO')
else:
    print('Seu ano não é BISSEXTO')