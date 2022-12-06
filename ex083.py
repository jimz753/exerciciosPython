aberto = fechado = 0
equaçao = (str(input('Digite uma equação para ser validada: ')))
equaçao.split()
for elemento in range(0, len(equaçao)):
    if equaçao[elemento] in '(':
        aberto += 1
    if equaçao[elemento] in ')':
        fechado += 1
if aberto == fechado:
    print('A sua equação é válida!')
else:
    print('A sua equação não é válida!!')