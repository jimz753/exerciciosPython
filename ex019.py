import random
a = input('Digite um nome: ')
b = input('Digite um segundo nome: ')
c = input('Digite um terceiro nome: ')
d = input('Digite um quarto nome: ')
lista = [a,b,c,d]
x = random.choice(lista)
print ('O nome sorteado foi {}'.format(x))