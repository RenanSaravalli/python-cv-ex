#Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.
jogador = {}
clube = []
gol = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for c in range(1,partidas+1):
        gol.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gol[:]
    total = sum(gol)
    jogador['total'] = total
    clube.append(jogador.copy())
    gol.clear()

    while True:
        resp = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! digite apenas S ou N')
    if resp in 'Nn':
        break
print('-='*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(clube):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para o programa!) '))
    if busca == 999:
        break
    if busca >= len(clube):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {clube[busca]["Nome"]}: ')
        for i, g in enumerate(clube[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('-- VOLTE SEMPRE --')