extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
posicao = int(input('Digite um número entre 0 e 20 para ver o seu nome: '))
while 0 < posicao > 20:
    posicao = int(input('Digite um número entre 0 e 20 para ver o seu nome: '))
print(f'Você digitou {posicao} e seu nome é {extenso[posicao]}')