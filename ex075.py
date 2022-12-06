num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um último número: ')))

if 9 in num:
    print(f'O número nove apareceu {num.count(9)} vezes')
else:
    print(f'Não foi digitado o número 9')
if 3 in num:
    print(f'O número três apareceu na {num.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print((n), end=' ')