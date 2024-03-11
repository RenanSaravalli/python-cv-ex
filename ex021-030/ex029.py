#Lê a velocidade de um carro. Se ele estiver acima de 80Km/h ele será multado. A multa vai custar R$7,00 por cada km acima do limite
vel = int(input('Qual era sua velocidade? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Sua velocidade era de {}Km/h e foi multado com uma multa de R${:.2f}'.format(vel, multa))
else:
    print('Sua velocidade de {}Km/h está dentro do limite da via '.format(vel))