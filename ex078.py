lista = list()
maior = menor = 0
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'Você digitou os valores {lista}, o maior valor foi {maior} na posição', end=' ')
for i, c in enumerate(lista):
    if c == maior:
        print(f'{i},', end=' ')
print(f'o menor valor foi {menor} na posição', end=' ')
for i, c in enumerate(lista):
    if c == menor:
        print(f'{i},', end=' ')