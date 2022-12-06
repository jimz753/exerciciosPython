print('Para criar uma Progressão Aritmética: ')
a1 = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
n = int(input('Quantos termos deseja que a progressão tenha? '))
n2 = 1
while n != 0:
    while n2 != n:
        a1 += r
        n2 += 1
        print ('{}º termo = {}'.format(n2, a1))
    n = int(input('Quantos termos deseja que a progressão tenha? '))
    if n < n2:
        n = 0