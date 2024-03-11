#Lê uma frase e diga se ela é um políndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
junto = ''.join(frase.split())
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print(junto, '->', inverso, end='')
    print('A frase {} invertida é um políndromo'.format(frase))
else:
    print(junto, '->', inverso, end='')
    print('A frase {} invertida não é um políndromo'.format(frase))