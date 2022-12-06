print('Vamos jogar JOKENPO???')
jogador = int(input("""JO
KEN...
1 ------> PEDRA
2 ------> PAPEL
3 ------> TESOURA
"""))
from random import choice

pedra = 1
papel = 2
tesoura = 3
lista = [1, 2, 3]

cpu = choice(lista)



if jogador == cpu :
    if jogador == 1:
        print('PO!!! Eu escolhi {}, você escolheu {} também, deu empate!!!'.format('PEDRA', 'PEDRA'))
    elif jogador == 2:
        print('PO!!! Eu escolhi {}, você escolheu {} também, deu empate!!!'.format('PAPEL', 'PAPEL'))
    elif jogador == 3:
        print('PO!!! Eu escolhi {}, você escolheu {} também, deu empate!!!'.format('TESOURA', 'TESOURA'))
else:
    if jogador == 1:
        if cpu == 2:
            print('PO!!! Eu escolhi {}, você escolheu {}, EU GANHEI!!XD'.format('PAPEL', 'PEDRA'))
        elif cpu ==3:
            print('PO!!! Eu escolhi {}, você escolheu {}, VOCÊ GANHOU!!:c'.format('TESOURA', 'PEDRA'))
    elif jogador == 2:
        if cpu == 1:
            print('PO!!! Eu escolhi {}, você escolheu {}, VOCÊ GANHOU!!:c'.format('PEDRA', 'PAPEL'))
        elif cpu == 3:
            print('PO!!! Eu escolhi {}, você escolheu {}, EU GANHEI!!XD'.format('TESOURA', 'PAPEL'))
    elif jogador == 3:
        if cpu == 1:
            print('PO!!! Eu escolhi {}, você escolheu {}, EU GANHEI!!XD'.format('PEDRA', 'TESOURA'))
        elif cpu == 2:
            print('PO!!! Eu escolhi {}, você escolheu {}, VOCÊ GANHOU!!:c'.format('PAPEL', 'TESOURA'))