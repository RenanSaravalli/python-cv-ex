#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições 


def voto(ano):
    from datetime import datetime # com a minha função declada apenas no escopo da minha função eu economizo a memória utilizada pelo programa isso pq só vou utilizar a função datetime dentro da minha função voto()
    idade = datetime.now().year - ano
    if idade >= 18 and idade < 65:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade == 16 or idade >=65:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return print(f'Com {idade} anos: VOTO NEGADO')
    


print('-'*20)
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
