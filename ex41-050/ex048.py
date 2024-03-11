#Calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
val = 0
print('Os números ímpares que são múltiplos de 3 entre 1 e 500 são:')
for c in range (1, 501):
    if c % 2 != 0 and c % 3 == 0:
        val = val + 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(val, soma))