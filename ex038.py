n1 = int(input('Para comparar qual é o maior entre dois valores, digite um dos valores: '))
n2 = int(input('Agora digite o outro valor: '))
if n1>n2:
    print('O maior valor é {}'.format(n1))
elif n2>n1:
    print('O maior valor é {}'.format(n2))
elif n1==n2:
    print('Nenhum dos valores é maior que o outro.')