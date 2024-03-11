def aumentar(valor = 0,porc = 0):
    aumento = valor + (valor * porc / 100)
    return aumento 


def diminuir(valor = 0,porc = 0):
    reduc = valor - (valor * porc / 100 )   
    return reduc


def dobro(valor = 0):
    mult = valor * 2
    return mult

def metade(valor = 0):   
    divid = valor / 2
    return divid

def moeda(preço = 0, moeda = 'R$'):
    formata = f'{moeda}{preço:>.2f}'.replace('.',',')
    return formata
    
