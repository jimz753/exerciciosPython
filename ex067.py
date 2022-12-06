while True:
    print('<=================TABUADA 2.0=================>')
    num = int(input('Digite um número inteiro para ver a sua tabuada: '))
    multip = 1
    if num < 0:
        print('Programa Encerrado')
        break
    while multip <= 10:
        print(f'{num} x {multip} = {num * multip}')
        multip += 1
