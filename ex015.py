d = float(input('Quantos dias você ficou com o carro?'))
k = float(input('Quantos kilometros o carro rodou?'))
n = (d*60)+(k*0.15)
print ('O valor total a pagar é de R${:.2f}'.format(n))