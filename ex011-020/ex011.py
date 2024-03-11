larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = 2   
quant = area / tinta
print('Sua parede tem a dimensão {}x{} e sua área é de {}m².'.format(larg,alt,area))
print('A quantidade de tinta necessária para pintar ela é {}L de tinta'.format(quant))