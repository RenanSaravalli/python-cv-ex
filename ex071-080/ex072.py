#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    while valor < 0 and valor > 20:
        valor = int(input('Digite um número entre 0 e 20: '))
    if valor >= 0 and valor <= 20:
        break

print(f'Você digitou o número {num[valor]}')
