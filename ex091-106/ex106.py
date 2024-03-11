# Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. 
def ajuda(h):
    while True:
        acess = input(h)
        if acess == 'fim':
            print('Até logo!!')
            break
        else:
            help(acess)
        
    
ajuda('Função ou Biblioteca > ')