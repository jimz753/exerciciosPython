from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    if (atual - ano) >= 18:
        totalmaior += 1
        print('Essa pessoa já atingiu a maioridade fazem cerca de {} anos'. format((atual - ano) - 18))
    else:
        totalmenor +=1
        print('Faltam cerca de {} anos para essa pessoa ser maior de idade'.format(18 - (atual - ano)))

print(' Ao todo teve {} pessoas que já atingiram a maioridade'.format(totalmaior))
print('e {} pessoas que ainda não atingiram.'.format(totalmenor))