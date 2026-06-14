dias = int(input("Digite o número de dias alugados: "))
km = float(input("Digite o número de kilometros rodados: "))
soma = (dias * 60) + (km * 0.15)
print("O valor total a ser pago é: R${:.2f}".format(soma))
