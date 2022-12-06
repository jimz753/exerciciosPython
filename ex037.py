n = int(input('Digite um número inteiro: '))
b = int(input('Agora escolha a base de conversão, digite: 1 para binário, 2 para octagonal e 3 para hexadecimal ---->'))
if b == 1:
    print('O número {} convertido em binário é {}'.format(n,bin(n)))
elif b == 2:
    print('O número {} convertido em octagonal é {}'.format(n,oct(n)))
elif b==3:
    print('O número {} convertido em hexadecimal é {}'.format(n,hex(n)))