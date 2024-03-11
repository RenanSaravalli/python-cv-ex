# Recebe Nome completo e devolve o nome com todas as letras maiúsculas; O nome com todas minúsculas; Quantas letras ao todo sem considerar espaços; Quantas letras tem o primeiro nome 

nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
dividido = ((nome.split()))
print('Seu primeiro nome possui {} letras'.format(len(dividido[0])))