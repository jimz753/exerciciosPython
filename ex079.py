lista = list()
while True:
    valor = int(input('Digite um valor numérico: '))
    while valor in lista:
       print('Valor repetido, não foi adicionado')
       valor = int(input('Digite um outro valor numérico: '))
    lista.append(valor)
    continuar = str(input('Deseja continuar (S/N)? ')).upper().strip()
    if continuar == 'N':
        break
lista.sort()
print(lista)