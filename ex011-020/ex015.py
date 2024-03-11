#Calcula aluguel de carros

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
precod = d * 60
precokm = km * 0.15
total = precokm + precod 
print('O total a pagar é de R${}'.format(total))
