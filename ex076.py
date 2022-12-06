lista = ('Miojo', 1.30,
         'Pão', 3,
         'Feijão', 8.5,
         'Arroz', 24.99,
         'Bacon', 8.99,
         'Tomate', 5.45)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end= '')
    else:
        print(f'{lista[pos]:>8.2f}')