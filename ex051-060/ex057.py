#Lê o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = input('Qual seu sexo [M/F]: ').upper().strip()
while sexo != 'M' and sexo != 'F':
    print('Digite apenas [M/F]')
    sexo = input('Qual seu sexo [M/F]: ')

if sexo == 'M':
    print('Sexo: Masculino')
elif sexo == 'F':
    print('Sexo Femenino.')