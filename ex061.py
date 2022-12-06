print('Para criar uma Progressão Aritmética de 10 termos')
a1 = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Digite a razão da progressão aritmética: '))
n = 1
while n != 10:
    a1 += r
    n += 1
    print ('{}º termo = {}'.format(n, a1))