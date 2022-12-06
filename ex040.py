n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
media = (n1 + n2)/2
if media < 5.0:
    print('Você foi reprovado :c')
elif media >= 5.0 and media <= 6.9:
    print('Você ficou em recuperação')
else:
    print('Você foi aprovado, parabéns!! :)')