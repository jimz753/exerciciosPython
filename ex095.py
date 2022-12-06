basedados = list()
jogador = dict()
partidas = list()
while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    totalpartidas = int(input('Digite o número de partidas: '))
    totalgol = 0
    partidas.clear()
    for n in range(0, totalpartidas):
        partidas.append(int(input(f'Digite quantos gols ele marcou na {n + 1}ª partida: ')))
        totalgol += partidas[n]
    jogador['Gols'] = partidas[:]
    jogador['Total de gols'] = totalgol
    basedados.append(jogador.copy())
    continuar = str(input('Deseja continuar [S/N]? ')).upper()
    if continuar in 'N':
        break
print('<=>' * 30)
print(f'{"Cod":<3}', end=' ')
for k in jogador.keys():
    print(f'{str(k):<20}', end='')
print()
print('_' * 60)
for k, v in enumerate(basedados):
    print(f'{k:<3}', end='')
    for c in v.values():
        print(f' {str(c):<20}', end='')
    print()
    print('_' * 60)
print('<=>' * 30)
while True:
    busca = int(input('Digite o código do jogador para pesquisar os seus dados (999 para encerrar): '))
    if busca == 999:
        break
    if busca > len(basedados):
        print('Erro! Não existe esse jogador')
    else:
        print(f'Pesquisa do jogador {basedados[busca]["Nome"]}:')
        for k, v in enumerate(basedados[busca]["Gols"]):
            print(f'No jogo {k} fez {v} gols.')
            print('_' * 60)
print('Encerrado')