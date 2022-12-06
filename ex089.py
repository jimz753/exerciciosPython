ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar [S/N]? '))
    if continuar in 'Nn':
        break
print('=' * 20 + '><' + '=' * 20)
print(f'{"Nº":<5}{"NOME":<20}{"MÉDIA":<5}')
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<20}{a[2]:<5}')
while True:
    num = int(input('Digite o número do aluno para ver suas notas (999 encerra o programa): '))
    if num == 999:
        break
    print(f'As notas de {ficha[num][0]} são {ficha[num][1]} ')