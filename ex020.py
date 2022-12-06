import random
a = input('Digite um nome: ')
b = input('Digite um segundo nome: ')
c = input('Digite um terceiro nome: ')
d = input('Digite um quarto nome: ')
lista = [a,b,c,d]
x = random.sample(lista,4)
print ('A ordem da apresentação é {}'.format(x))