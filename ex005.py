n = int(input('Olá, digite um número: '))
vm = '\033[1;31m'
vd = '\033[1;32m'
az = '\033[1;34m'
fc = '\033[m'
print ('O predecessor de {}{}{} é {}{}{} e o sucessor é {}{}{}'.format(vm,n,fc,vd,n-1,fc,az,n+1,fc))