lista = list()
while True:
    lista.append(int(input('Digite um valor numérico: ')))
    continuar = str(input('Deseja continuar (S/N)? ')).upper().strip()
    if continuar in 'N':
        break
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {lista}.')
if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')