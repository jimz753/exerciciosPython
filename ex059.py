print('PROGRAMA DE ARITMÉTICA BÁSICA:')
x = float(input('Digite um número: '))
y = float(input('Digite um número: '))
menu = int(input('''Agora escolha o que deseja fazer com esses valores:
 Digite:
 1 -> SOMA
 2 --> MULTIPLICAÇÃO
 3 ---> QUAL O MAIOR
 4 ----> DIGITE NOVOS NÚMEROS
 5 -----> ENCERRAR PROGRAMA
 '''))

while menu != 5:
    if menu == 1:
        print('O valor da soma entre {} e {} é {}'.format(x,y, x + y))
        menu = int(input('''Escolha uma nova opção:
         Digite:
         1 -> SOMA
         2 --> MULTIPLICAÇÃO
         3 ---> QUAL O MAIOR
         4 ----> DIGITE NOVOS NÚMEROS
         5 -----> ENCERRAR PROGRAMA
         '''))
    elif menu == 2:
        print('O valor da multiplicação entre {} e {} é {}'.format(x, y, x * y))
        menu = int(input('''Escolha uma nova opção:
                 Digite:
                 1 -> SOMA
                 2 --> MULTIPLICAÇÃO
                 3 ---> QUAL O MAIOR
                 4 ----> DIGITE NOVOS NÚMEROS
                 5 -----> ENCERRAR PROGRAMA
                 '''))
    elif menu == 3:
        if x > y:
            print('O maior valor entre {} e {} é {}'.format(x, y, x))
            menu = int(input('''Escolha uma nova opção:
                     Digite:
                     1 -> SOMA
                     2 --> MULTIPLICAÇÃO
                     3 ---> QUAL O MAIOR
                     4 ----> DIGITE NOVOS NÚMEROS
                     5 -----> ENCERRAR PROGRAMA
                     '''))
        else:
            print('O maior valor entre {} e {} é {}'.format(x, y, y))
            menu = int(input('''Escolha uma nova opção:
                     Digite:
                     1 -> SOMA
                     2 --> MULTIPLICAÇÃO
                     3 ---> QUAL O MAIOR
                     4 ----> DIGITE NOVOS NÚMEROS
                     5 -----> ENCERRAR PROGRAMA
                     '''))
    elif menu == 4:
        x = float(input('Digite um novo número: '))
        y = float(input('Digite um novo número: '))
        menu = int(input('''Escolha uma nova opção:
                             Digite:
                             1 -> SOMA
                             2 --> MULTIPLICAÇÃO
                             3 ---> QUAL O MAIOR
                             4 ----> DIGITE NOVOS NÚMEROS
                             5 -----> ENCERRAR PROGRAMA
                             '''))