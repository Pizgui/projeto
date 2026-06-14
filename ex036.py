vcasa = int(input('Qual o valor da casa que você quer comprar? '))
salario = int(input('Qual o seu salário atual? '))
tempo = int(input('quantos anos de financiamento '))
mensalidade = vcasa / (tempo*12)
if mensalidade > 0.3 * salario:
    print('A mensalidade ultrapassa 30% do seu salário, não é possível fazer a compra.')
else:
    print('O valor da mensalidade é {}'.format(mensalidade))