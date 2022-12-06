lista = list()
for indice in range(0, 5):
    valor = int(input('Digite um valor numérico: '))
    if indice == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                break
            posicao += 1
print(lista)
