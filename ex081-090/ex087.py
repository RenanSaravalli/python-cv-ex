#Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha. 
matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = soma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Dgite um valor para a posição [{l}, {c}]: '))
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
print('-='*20)

for lista in matriz:
    for num in lista:
        if num % 2 == 0:
            par += num
print(f'A soma dos valores pares é {par}.')

for lista in matriz:
    soma += lista[2]    
        
print(f'A soma dos valores da terceira coluna é {soma}.')

print(f'O maior valor da segunda linha é {max(matriz[1])}.')