num = cont = somat = 0
while True:
    num = int(input(f'Digite um número inteiro (999 para encerrar): '))
    if num == 999:
        break
    cont += 1
    somat += num
print(f'Foram digitados {cont} números e a soma entre eles foi de {somat}')