frase = str(input('Digite uma frase para descobrir se ela é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
print(junto, inverso)