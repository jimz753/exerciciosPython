from random import randint
from time import sleep
numeros = list()


def sorteia():
    for n in range(0, 5):
        numeros.append(randint(0, 9))
    print('Sorteando os 5 valores da lista: ', end='')
    for c in numeros:
        print(f'{c} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somaPar():
    par = 0
    for c in numeros:
        if c % 2 == 0:
           par += c
    print(f'Somando os valores pares de {numeros}, temos {par}.')


sorteia()
somaPar()