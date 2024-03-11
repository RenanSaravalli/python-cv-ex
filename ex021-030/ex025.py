#Verifica se o nome da pessoa possui Silva

nome = input('Qual seu nome? ')

if ('SILVA' in nome.upper()):
    print('O seu nome {} possui Silva'.format(nome))
else: 
    print('O seu nome {} não possui Silva'.format(nome))