from random import randint
r = randint(0,5)
num = int(input('Pensei em um número de 0 a 5, tente adivinhar: '))
if (num == r):
    print('Parabéns, você acertou!!')
else:
    print('Você errou! O número que eu escolhi foi {}'.format(r))
print('Foi bom jogar com você!')