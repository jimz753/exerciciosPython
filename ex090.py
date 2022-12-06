dicionario = dict()
dicionario['Nome'] = str(input('Digite o nome do aluno: '))
dicionario['Média'] = float(input('Digite a média do aluno: '))
if dicionario['Média'] >= 5:
    dicionario['Situação'] = 'Aprovado'
else:
    dicionario['Situação'] = 'Reprovado'
print(f'A média do aluno {dicionario["Nome"]} foi {dicionario["Média"]} e a situação é de {dicionario["Situação"]}')