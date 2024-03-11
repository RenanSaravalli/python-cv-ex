def aumentar(valor = 0,porc = 0, sit = False):
    aumento = valor + (valor * porc / 100)
    if sit == False:
        return aumento
    else:
        return moeda(aumento)


def diminuir(valor = 0,porc = 0, sit = False):
    reduc = valor - (valor * porc / 100 )   
    if sit == False:
        return reduc
    else:
        return moeda(reduc)


def dobro(valor = 0, sit = False):
    mult = valor * 2
    if sit == False:
        return mult
    else:
        return moeda(mult)
    

def metade(valor = 0, sit = False):   
    divid = valor / 2
    if sit == False:
        return divid
    else:
        return moeda(divid)
    
def moeda(preço = 0, moeda = 'R$'):
    formata = f'{moeda}{preço:>.2f}'.replace('.',',') 
    return formata
    
