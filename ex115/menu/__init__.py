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

def linha(tam = 42):
    return '-' * tam

def cabeçalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1  
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
