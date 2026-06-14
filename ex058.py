from random import randint
c = 0
r = randint(0,5)
num = int(input('Pensei em um número de 0 a 5, tente adivinhar: '))
while num != r:
    tn = int(input('Não é esse, tente novamente: '))
    num = tn
    c + 1
print('Parabéns, você acertou!!')
