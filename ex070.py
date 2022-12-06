pessoa = caro = barato = soma = 0
nomebarato = ''
while True:
    pessoa += 1
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    soma += preço
    if pessoa == 1 or preço < barato:
        barato = preço
        nomebarato = nome
    if preço > 1000:
        caro += 1
    continuar = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'''A soma total dos produtos foi de R${soma:.2f}, {caro} produtos custaram mais de R$1000.00 reais
e o nome do produto mais barato é {nomebarato}''')