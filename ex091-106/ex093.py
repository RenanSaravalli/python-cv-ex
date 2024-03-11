#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
gol = []
total = 0

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for c in range(1, partidas+1):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['Gols'] = gol[:]

for g in jogador['Gols']:
    total += g # poderia utilizar o sum(gol) que iria somar todos os items dentro da lista
jogador['Total'] = total

print('-='*30)
print(jogador)
print('-='*30)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')

for c in range(0, partidas):
    print(f'=> Na partida {c+1}, fez {gol[c]}')
print(f'Foi um total de {total} gols.') 