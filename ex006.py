n = float(input('Oi, digite um número: '))
vm = '\033[1;31m'
vd = '\033[1;32m'
az = '\033[1;34m'
rx = '\033[1;35m'
fc = '\033[m'
print('O dobro de {}{}{} é {}{:.0f}{}, o triplo é {}{:.0f}{} e a sua raiz quadrada {}{}{}'.format(rx,n,fc,vm,n*2,fc,vd,n*3,fc,az,n**1/2,fc))