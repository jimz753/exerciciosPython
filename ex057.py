sexo = str(input('Digite qual o seu sexo (M/F): ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Digite qual o seu sexo (M/F): ')).upper().strip()
print('Sexo {} registrado'.format(sexo))