individuo = dict()
grupo = list()
soma = 0
while True:
    individuo['Nome'] = str(input('Nome: '))
    individuo['Sexo'] = str(input('Sexo (M/F/NB): ')).upper()
    if individuo['Sexo'] not in 'MFNB':
        individuo['Sexo'] = str(input('Erro!Responda apenas (M/F/NB): '))
    individuo['Idade'] = int(input('Idade: '))
    grupo.append(individuo.copy())
    soma += individuo['Idade']
    continuar = str(input('Deseja continuar (S/N)? ')).upper()
    if continuar not in 'SN':
        continuar = str(input('Erro! Responda apenas (S/N): ')).upper()
    if continuar in 'N':
        break
media = soma / len(grupo)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f}.')
print(f'C) As mulheres cadastradas na lista são:')
for c in grupo:
    if c['Sexo'] in 'F':
        print(f'    => {c["Nome"]}')
print(f'D) Lista das pessoas com idade acima da média:')
for c in grupo:
    for k, v in c.items():
        print(f'    {k} = {v}; ', end='')
    print()
print('<==TERMINADO==>')