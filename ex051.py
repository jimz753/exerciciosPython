print('Para criar uma Progressão Aritmética de 10 termos')
a1 = int(input('Digite o primeiro termo da progressão aritmética: '))
d = int(input('Digite a razão da progressão aritmética: '))
n = int(input('Digite o número de termos que deseja: '))
an = a1 + (n-1)*d
for pa in range (a1, an, d):
    print(pa)