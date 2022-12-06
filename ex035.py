a = int(input('Digite uma das medidas para um triângulo qualquer: '))
b = int(input('Digite outra das medidas para um triângulo qualquer: '))
c = int(input('Digite a última das medidas para um triângulo qualquer: '))
if ( b - c ) < a < b + c and ( a - c ) < b < a + c and ( a - b ) < c < a + b:
    print('As medidas {}, {} e {} formam um triângulo!'.format(a,b,c))
else:
    print('As medidas {}, {} e {} NÃO formam um triângulo'.format(a,b,c))