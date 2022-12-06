jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Digite o nome do jogador: '))
totalpartidas = int(input('Digite o número de partidas: '))
totalgol = 0
for n in range(0, totalpartidas):
    partidas.append(int(input(f'Digite quantos gols ele marcou na {n + 1}ª partida: ')))
    totalgol += partidas[n]
jogador['Gols'] = partidas[:]
jogador['Total de gols'] = totalgol
print('<=>' * 30)
print(jogador)
print('<=>' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('<=>' * 30)
print(f'O jogador {jogador["Nome"]} jogou {totalpartidas}')
for c, g in enumerate(partidas):
    print(f'Na partida {c + 1}, fez {g} gol.')