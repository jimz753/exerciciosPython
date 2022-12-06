maiores = homem = mulher = 0
while True:
    print('#=======CADASTRO=======#')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa (M/F): ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if sexo == 'M':
        homem += 1
    continuar = str(input('Deseja continuar a cadastrar? (S/N): ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a cadastrar? (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastrados {maiores} pessoas maiores de 18 anos, {homem} homens de qualquer idade e {mulher} mulheres com menos de 20 anos.')