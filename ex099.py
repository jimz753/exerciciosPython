from time import sleep


def analise(* num):
    maior = contador = 0
    print('-=-' * 30)
    for n in num:
        print(f'{n} ', end='')
        sleep(0.5)
    print(f'Foram informados ao todo {len(num)} números.')
    for n in num:
        if contador == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        contador += 1
    print(f'O maior valor informado foi {maior}')
    print('-=-' * 30)


analise(7, 3, 4, 8, 6)
analise(3, 4, 9)
analise(2, 1)
analise(6)
analise()