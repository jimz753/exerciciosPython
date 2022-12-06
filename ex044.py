print('Para saber o valor do produto considerando a forma de pagamento, digite ')
p = float(input('O preço normal do produto: '))
f = int(input("""Para a forma de pagamento, digite: 1 para dinheiro, 2 para cartão de débito, 
3 para até 2 vezes no crédito e 4 para mais de 3 vezes no crédito ---->  """))
if f == 1:
    print('Pagamento em dinheiro, o valor com desconto fica R${:.2f}'.format(p*0.9))
elif f == 2:
    print('Pagamento em cartão de débito, o valor com desconto fica R${:.2f}'.format(p * 0.95))
elif f == 3:
    print('Pagamento em até 2 vezes no crédito, o valor fica R${:.2f}'.format(p))
else:
    print('Pagamento em 3 vezes ou mais no crédito, o valor com juros fica R${:.2f}'.format(p*1.2))