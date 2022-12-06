print('CALCULADORA DE FATORIAl!')
numero = int(input('Digite um número natural para calcular o seu fatorial: '))
numeromenos = numero - 1
fatorial = numero
while numeromenos != 0:
    fatorial *= numeromenos
    numeromenos -= 1
print('O fatorial de {} é {}'.format(numero, fatorial))