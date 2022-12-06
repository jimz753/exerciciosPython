x = float(input('Digite um número: '))
y = float(input('Mais um número: '))
z = float(input('Mais um número: '))
if x > y and x>z:
    maior = x
if y > x and y>z:
    maior = y
if z > y and z>x:
    maior = z
if x < y and x<z:
    menor = x
if y < x and y<z:
    menor = y
if z < y and z<x:
    menor = z
print('{} é o maior número.'.format(maior))
print('{} é o menor número.'.format(menor))