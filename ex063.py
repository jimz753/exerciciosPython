n = int(input('Digite o número de termos da sequência de Fibonacci que deseja demonstrar: '))
ct = 0
f1 = 0
f2 = 1

if n <= 0:
    print('Digite um número positivo')
    n = int(input('Digite o número de termos da sequência de Fibonacci que deseja demonstrar: '))

elif n == 1:
    print('O {}º termo de Fibonacci é {}'.format(n, f1))

else:
    while ct < n:
        print('O {}º termo de Fibonacci é {}'.format(ct + 1, f1))
        f = f1 + f2
        f1 = f2
        f2 = f
        ct += 1