completa = list()
pares = list()
impares = list()
while True:
    valor = (int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
    completa.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    if continuar in 'N':
        break
print(f'A lista com todos os números digitado é {completa}, a lista dos números pares digitados é {pares} '
      f'e a lista dos impares é {impares}.')