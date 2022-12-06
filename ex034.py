sal = float(input('Para saber o valor do aumento, digite o seu sálario atual: '))
if sal<=1250:
    x = sal*1.15
else:
    x = sal*1.1
print('O seu novo sálario é de R${:.2f}'.format(x))