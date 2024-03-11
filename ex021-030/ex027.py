#Lê nome de uma pessoa, mostrando em seguida o primeiro e o último nome Separadamente 
nome = input('Qual é o seu nome? ')
dividi = nome.strip().split()
print('Seu nome completo é {}'.format(nome))
print('Seu Primeiro nome é {}'.format(dividi[0]))
print('Seu Útimo nome é {}'.format(dividi[-1]))