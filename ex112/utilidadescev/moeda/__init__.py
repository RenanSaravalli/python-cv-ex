def aumentar(valor = 0,porc = 0, sit = True):
    aumento = valor + (valor * porc / 100)
    if sit == False:
        return aumento
    else:
        return moeda(aumento)


def diminuir(valor = 0,porc = 0, sit = True):
    reduc = valor - (valor * porc / 100 )   
    if sit == False:
        return reduc
    else:
        return moeda(reduc)


def dobro(valor = 0, sit = True):
    mult = valor * 2
    if sit == False:
        return mult
    else:
        return moeda(mult)
    

def metade(valor = 0, sit = True):   
    divid = valor / 2
    if sit == False:
        return divid
    else:
        return moeda(divid)
    
def moeda(preço = 0, moeda = 'R$'):
    formata = f'{moeda}{preço:>.2f}'.replace('.',',') 
    return formata
    
def resumo(preço = 0, cres = 0, decres = 0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)

    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço)}')
    print(f'Metade do preço: \t{metade(preço)}')
    print(f'{cres}%, de aumento: \t{aumentar(preço, cres)}')
    print(f'{decres}%, de redução: \t{diminuir(preço,decres)}')
    print('-' * 35)


