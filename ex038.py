n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))

if n1 > n2:
    print('{} é o maior número, pois vale mais que {}.'.format(n1,n2))
elif n2 > n1:
    print('{} é o maior número, pois vale mais que {}.'.format(n2,n1))
else:
    print('Não há número maior, os dois números são de valor igual.')