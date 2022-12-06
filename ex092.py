cadastro = dict()
cadastro['Nome'] = str(input('Digite o nome: '))
cadastro['Sexo'] = str(input('Digite o sexo(M/F): ')).upper()
cadastro['Idade'] = int(input('Digite a idade: '))
cadastro['CTPS'] = int(input('Digite a Carteira de Trabalho: '))
if cadastro['CTPS'] == 0:
    for k, v in cadastro.items():
        print(f'a chave {k} tem o valor {v}')
else:
    cadastro['Ano de contração'] = int(input('Digite o ano da contratação: '))
    cadastro['Sálario'] = int(input('Digite o atual sálario: '))
if cadastro['Sexo'] in 'M':
    cadastro['Aposentadoria'] = 65 - cadastro['Idade']
    for k, v in cadastro.items():
        print(f'A chave {k} tem o valor {v}')
else:
    cadastro['Aposentadoria'] = 62 - cadastro['Idade']
    for k, v in cadastro.items():
        print(f'A chave {k} tem o valor {v}')