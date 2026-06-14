velocidade = int(input('Informe a velocidade do carro: '))
if velocidade > 80:
    valor = ((velocidade-80) * 7)
    print('Você foi multado, o valor da multa foi de R${}'.format(valor))
else:
    print('Muito bem, você andou dentro do limite de velocidade.')