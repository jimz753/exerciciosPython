lista = [[], []]
for indice in range(0, 7):
    valor = int(input(f'Digite o {indice + 1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os números pares foram {lista[0]} e os ímpares foram {lista[1]}.')