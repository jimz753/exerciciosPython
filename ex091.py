from random import randint
from operator import itemgetter
rank = dict()
jogo = dict()
for c in range(0, 4):
    jogo[f'Jogador {c + 1}'] = randint(1, 6)
for k,v in jogo.items():
    print(f'O {k} tirou {v}')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(rank)