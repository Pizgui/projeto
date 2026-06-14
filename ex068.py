from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
soma = jgoador = computador = vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    soma = computador + jogador
    opc = ''
    opc = str(input('Par ou Ímpar? [P/I] '))
    while opc not in 'IiPp':
        opc = str(input('Par ou Ímpar? [P/I] '))
    print('-'*30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {soma}.', end='')
    print('DEU PAR' if soma %2 ==0 else 'DEU ÍMPAR.')
    print('-'*30)
    if opc in 'Pp':
        if soma%2 == 0:
            vitorias += 1
            print('VOCÊ VENCEU!!')
            print('Vamos jogar de novo...')
            print('=-'*15)
        else:
            print('VOCÊ PERDEU!!')
            print(f'GAME OVER! Você venceu {vitorias} vezes.')
            break
    elif opc in 'Ii':
        if soma%2 == 1:
            vitorias += 1
            print('VOCÊ VENCEU!!')
            print('Vamos jogar de novo...')
            print('=-'*15)
        else:
            print('VOCÊ PERDEU!!')
            print(f'GAME OVER! Você venceu {vitorias} vezes.')
            break