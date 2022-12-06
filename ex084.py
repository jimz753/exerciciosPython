dados = list()
lista = list()
pesado = leve = 0
nomepesado = nomeleve = ''
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso em Kgs: ')))
    if len(dados) == 0:
        pesado = dados[1]
        leve = dados[1]
        nomepesado = dados[0]
        nomeleve = dados[0]
    else:
        if dados[1] >= pesado:
                pesado = dados[1]
                nomepesado = dados[0]
        if dados[1] <= leve:
                leve = dados[1]
                nomeleve = dados[0]
    lista.append(dados[:])
    dados.clear()
    continuar = input(str('Deseja continuar?(S/N) ')).upper().split()
    if 'N' in continuar:
        break
print(f'Você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi {pesado}Kgs de {nomepesado}')
print(f'O menor peso foi {leve}Kgs de {nomeleve}')