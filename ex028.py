import random
x = int(random.choice([0,1,2,3,4,5]))
z = int(input('Digite um número entre 0 e 5: '))
print('O número pensado foi {}'.format(x))
print('Parabéns, você acertou!!!' if x == z else 'Tente novamente.')