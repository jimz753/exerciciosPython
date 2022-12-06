n = input ('digite algo:')
bc = '\033[1;30m'
vm = '\033[1;31m'
vd = '\033[1;32m'
al = '\033[1;33m'
az = '\033[1;34m'
rx = '\033[1;35m'
cy = '\033[1;36m'
fc = '\033[m'
print ('{}É uma letra?'.format(bc),n.isalpha(),'{}'.format(fc))
print ('{}É um alfanumeral?'.format(vm),n.isalnum(),'{}'.format(fc))
print ('{}É decimal?'.format(vd),n.isdecimal(),'{}'.format(fc))
print ('{}É em formatação ASCII?'.format(al),n.isascii(),'{}'.format(fc))
print ('{}É um dígito?'.format(az),n.isdigit(),'{}'.format(fc))
print ('{}É um identificador?'.format(rx),n.isidentifier(),'{}'.format(fc))
print ('{}Está em minúsculas?'.format(cy),n.islower(),'{}'.format(fc))
print ('{}É um numeral?'.format(bc),n.isnumeric(),'{}'.format(fc))
print ('{}Pode ser impresso?'.format(vm),n.isprintable(),'{}'.format(fc))
print ('{}É um espaço vazio?'.format(vd),n.isspace(),'{}'.format(fc))
print ('{}É um título?'.format(al),n.istitle(),'{}'.format(fc))
print ('{}Está em maiúsculas?'.format(az),n.isupper(),'{}'.format(fc))
