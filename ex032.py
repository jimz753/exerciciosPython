ano = int(input('Digite um ano: '))
print ('Esse ano é bissexto' if ano%4==0 and ano%100!=0 else 'Esse ano não é bissexto')