#Lê o peso e a altura da pessoa e calcule seu imc e mostre seu status, de acordo com a tabeta: abaixo de 18.5: abaixo do peso, entre 18.5 e 25: peso ideal, 25 até 30: Sobrepeso, 30 até 40: Obesidade, Acima de 40: Obesidade mórbida.
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura em metros? '))
imc = peso / (altura **2)

if imc < 18.5:
    print('Seu imc é {:.2f} e você está Abaixo do peso'.format(imc))
elif imc < 25:
    print('Seu imc é {:.2f} e você está com Peso ideal'.format(imc))
elif imc < 30:
    print('Seu imc é {:.2f} e você está com Sobrepeso'.format(imc))
elif imc < 40:
    print('OSeu imc é {:.2f} e você está com Obesidade'.format(imc))
else:
    print('Seu imc é {:.2f} e você está com Obesidade Mórbida'.format(imc))