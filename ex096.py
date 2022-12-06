def area(a, b):
    quadrado = a * b
    print(f'A área de um terreno {a}x{b} é de {quadrado:.2f}m².')


a = float(input('Digite a altura em metros: '))
b = float(input('Digite a largura em metros: '))
area(a, b)