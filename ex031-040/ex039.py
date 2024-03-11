#Lê o ano de nascimento de um jovem e informe de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar, -se é a hora de se alistar, -Se já passou do tempo do alistamento. 
nasc = int(input('Olá jovem, em que ano você nasceu? '))
anoAtual = 2024

if anoAtual - nasc == 18:
    print('Neste ano você completará 18 anos então está na hora de se alistar no serviço militar!')
elif anoAtual - nasc < 18:
    falta = anoAtual - nasc
    falta = 18 - falta
    print('Você ainda não possui 18 anos, então daqui {} anos terá que se alistar no serviço militar!'.format(falta))
else:
    print('Você já passou dos 18 anos espero que já tenha se alistado ao serviço militar!')