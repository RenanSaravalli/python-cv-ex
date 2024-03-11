#Pergunta a distância de uma viagem em Km. Calcula o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas. 
km = int(input('Qual a distância em Km de sua viagem? '))
if km <= 200:
    preco = km * 0.50
    print('A sua viagem de {}km vai custar R${:.2f}'.format(km,preco))
else:
    Npreco = km * 0.45
    print('A sua viagem de {}km vai custar R${:.2f}'.format(km,Npreco))