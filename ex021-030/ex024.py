#Verifica se a cidade começa com o nome santo

cidade = input('Qual o nome da sua cidade? ')
dividi = cidade.split()
if dividi[0] == 'Santo':
    print('O nome da sua cidade começa com Santo')
else:
    print('O nome da sua cidade não começa com Santo')