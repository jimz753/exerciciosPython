import datetime
ano = int(input('Para maiores informações sobre o alistamento de 2020, digite o seu ano de nascimento: '))
idade = 2020 - ano
prazo = datetime.datetime(2020, 9, 30, 23, 59, 59)
hoje = datetime.datetime.today()

if idade < 18:
    print('Você ainda não precisa se alistar')
elif idade == 18 and hoje < prazo:
    print('Esse é o seu ano de alistamento, o prazo para se alistar expira em {}'.format(hoje - prazo))
elif idade == 18 and hoje > prazo:
    print('Esse era o seu ano de alistar, o prazo expirou por {} horas'.format(hoje - prazo))
else:
    print('Você deveria ter se alistado {} anos atrás'.format(idade - 18))