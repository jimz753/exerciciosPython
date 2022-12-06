palavras = ('JESUS', 'JESSIE', 'TULIP', 'HUMPERDOO', 'HERR', 'KLAUS', 'STARR',
            'ARCHMEDIAN', 'BUSTER', 'SURLY', 'JOE')
for pos in range (0, len(palavras)):
    print(f'\nNa palavra {palavras[pos]} temos as vogais:', end=' ')
    for letra in palavras[pos]:
        if letra in 'AEIOU':
            print(letra, end=' ')