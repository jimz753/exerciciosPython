import math
x = int(input('Digite um ângulo:'))
s = math.sin(x)
c = math.cos(x)
t = math.tan(x)
print('Dado o ângulo {}, temos o seno {}, o coseno {} e a tangente {}'.format(x,math.ceil(s),math.ceil(c),math.ceil(t)))
