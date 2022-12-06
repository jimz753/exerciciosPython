n = float(input('Qual a velocidade do veículo? '))
print ( 'Você foi multado em R${:.2f} por passar do limite de velocidade.'.format((n-80)*7)if n>=80 else 'Tudo certo!')