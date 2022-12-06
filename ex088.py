from random import randint
print('='* 10 + '>GERADOR DE MEGA SENA<' + '='* 10)
n = int(input('Quantos jogos você deseja gerar:? '))
lista = list()
jogo = list()
for indice in range(0, n):
    for numero in range (0, 6):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
print(f'Foram sorteados {n} jogos e eles são')
for i, l in enumerate(jogo):
    print(f'Jogo {i + 1}: {l}')