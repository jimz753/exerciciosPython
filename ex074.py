from random import randint
num = randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)
maior = menor = 0
for posi, elemento in enumerate(num):
    if posi == 0:
        maior = elemento
        menor = elemento
    else:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento
print(f'Os valores sorteados foram {num}, o maior valor foi {maior} e o menor valor foi {menor}')
