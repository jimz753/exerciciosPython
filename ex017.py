from math import hypot
x = float(input('Coloque o comprimento de um cateto:'))
y = float(input('Agora coloque o comprimento do outro cateto:'))
s = hypot(x,y)
print('A hipotênusa dos catetos {} e {} é igual a {}'.format(x,y,s))