import random
cpu = 0
jogador = 1
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tentativas = 0
print('*===== J060 D4 4DV1NH4ÇÃ0 2.0 =====* ')
print('Vamos se divertir? Eu vou pensar num número entre 0 e 10.')
print('Você tem que advinhar')
while cpu != jogador:
    cpu = random.choice(lista)
    jogador = int(input('Pronto? Qual o número que estou pensando? '))
    tentativas += 1
    print('Eu pensei {} e você respondeu {}, foram {} tentativas'.format(cpu, jogador, tentativas))