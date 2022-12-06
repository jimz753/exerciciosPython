contador = 0
somatoria = 0
n = int(input('Digite um número inteiro (999 encerra o programa): '))
while n != 999:
    somatoria += n
    contador += 1
    n = int(input('Digite um número inteiro (999 encerra o programa): '))
print('Foram digitados {} números e a soma entre eles é de {}'.format(contador, somatoria))