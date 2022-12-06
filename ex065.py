maior = 0
menor = 0
contador = 0
somatoria = 0
continuar = ''
while continuar != 'N':
    n = int(input('Digite um número inteiro: '))
    somatoria += n
    contador += 1
    media = somatoria / contador
    if contador == 1:
        maior = n
        menor = n
    elif contador > 1:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('''Foram lidos {} números, a soma total deles foi de {}, 
a média dos valores foi de {:.2f}, o maior valor foi {} e o menor foi {}'''.format(contador, somatoria, media, maior, menor))