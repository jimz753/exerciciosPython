x = float(input('Qual a distância da viagem em Km? '))
print('O valor da viagem será de R${:.2f}'.format(x*0.5) if x<=200 else 'O valor da viagem será de R${:.2f}'.format(x*0.45))