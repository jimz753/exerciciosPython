from time import sleep


def contador(a, b, c):
    if c == 0:
        c = 1
    if c < 0 or a > b:
        c *= -1
    print('<->' * 30)
    if a < b:
        for n in range(a, b+1, c):
            print(f'{n}', end=' ')
            sleep(0.5)
    else:
        for n in range(a, b-1, c):
            print(f'{n}', end=' ')
            sleep(0.5)
    print('FIM')


#contador(1, 10, 1)
contador(10, 1, 2)
print('<->' * 30)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))