from math import floor, ceil
print('===---CAIXA_ELETRÔNICO---===')
valor = (int(input('Digite o valor que deseja sacar: R$')))
total = valor
nota = 50
totnotas = 0
while True:
    if total >= nota:
        total -= nota
        totnotas += 1
    else:
        if totnotas > 0:
            print(f'total de {totnotas} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnotas = 0
        if total == 0:
            break