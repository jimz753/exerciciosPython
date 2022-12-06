nome = input('Digite seu nome completo: ').strip()
n = nome.split()
n2 = len(n)
print ('O seu primeiro nome é {} e seu último é {}.'.format(n[0],n[n2-1]))
