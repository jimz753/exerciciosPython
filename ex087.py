matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = somatres = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para a posição [{l, c}]: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            par += valor
        if matriz[l][2]:
            somatres += matriz[l][2]
        if matriz[1][0]:
            maior = matriz[1][0]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é de {par}')
print(f'A soma dos valores da terceira coluna é {somatres}')
print(f'O maior valor da segunda linha foi {maior}')