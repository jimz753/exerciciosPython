homem = 'homem'
mulher = 'mulher'
nomevelho = ''
maioridade = 0
soma = 0
mulhernova = 0
for pessoa in range (1, 5):
    print('===== {}ª PESSOA ====='.format(pessoa))
    nome = str(input('Digite o nome: ')).capitalize()
    sexo = str(input('Digite o sexo (homem/mulher): ')).lower()
    idade = int(input('Digite a idade : '))
    soma += idade
    if pessoa == 1 and sexo == homem:
        maioridade = idade
        nomevelho = nome
    if idade > maioridade and sexo == homem:
            maioridade = idade
            nomevelho = nome
    if sexo == mulher and idade < 20:
        mulhernova += 1

print('A média de idade é de {:.1f} anos'.format(soma/4))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridade))
if mulhernova > 1:
    print('Tem {} mulheres menores de 20 anos'.format(mulhernova))
elif mulhernova == 1:
    print('Tem uma mulher menor de 20 anos')
else:
    print('Não tem mulheres menores de 20 anos')