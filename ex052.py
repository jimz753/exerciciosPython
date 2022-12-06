n = int(input('Para descobrir se um número inteiro é primo, digite ele: '))
tot = 0

for c in range(1, n+1):
    if n % c == 0:
        tot += 1

if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')