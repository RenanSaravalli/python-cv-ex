#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também a função leiaFlooat() com a mesma funcionalidade
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite o número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número!')
            return 0 
        else:
            return n 


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('ERRO, Digite um número real válido')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o número!')
            return 0 
        else:
            return n 


i = leiaInt('Digite um inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
 