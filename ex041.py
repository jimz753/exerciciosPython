import datetime
print('Para descobrir a sua categoria de natação')
dia = int(input('Digite o dia em que você nasceu: '))
mes = int(input('Digite o mês em que você nasceu: '))
ano = int(input('Digite o ano em que você nasceu: '))
idade = datetime.date.today().year - ano
realmes = datetime.date.today().month - mes
realdia = datetime.date.today().day - dia
if realmes < 0:
    idade = idade - 1
elif realdia < 0 and realmes == 0:
    idade = idade - 1
if idade <= 9:
    print('A sua categoria é Mirim')
elif 9 < idade <= 14:
    print('A sua categoria é Infantil')
elif 14 < idade <= 19:
        print('A sua categoria é Junior')
elif 19 < idade <= 20:
    print('A sua categoria é Senior')
else:
    print('A sua categoria é Master')