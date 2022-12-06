print('Para saber seu IMC, digite:')
peso = float(input('Seu peso em kilogramas: '))
altura = float(input('Sua altura em metro: '))
imc = peso/altura**2
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está muito abaixo do peso ideal'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é {:.1f}, você está no seu peso IDEAL'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.1f}, você está um pouco acima do seu peso ideal'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.1f}, você está obeso'.format(imc))
else:
    print('Seu IMC é {:.1f}, você está com obesidade mórbida'.format(imc))