import random
print('<=====Jogo do par ou ímpar=====>')
cpu = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
vitoria = derrota = 0
while derrota == 0:
    jogador = int(input('Digite um número par ou impar: '))
    escolha = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()[0]
    soma = jogador + cpu
    if escolha == 'P' and (soma) % 2 == 0:
        vitoria += 1
        print(f'''Você escolheu {jogador} e o computador {cpu}, a soma deu {soma}, foi PAR!
VOCÊ VENCEU''')
    elif escolha == 'I' and (soma) % 2 != 0:
        vitoria += 1
        print(f'''Você escolheu {jogador} e o computador {cpu}, a soma deu {soma}, foi ÍMPAR!
        VOCÊ VENCEU''')
    else:
        derrota += 1
print(f'''Você escolheu {jogador} e o computador {cpu}, a soma deu {soma},  
Você perdeu! Você venceu {vitoria} vezes!''')