lista = []
resp = 's'
resp = str(input('Quer adicionar um número na lista?(S/N) '))
if resp in 'Ss':
    while True:
        num = int(input('Digite um número: '))
        lista.append(num)
        resp = str(input('Quer adicionar mais um número na lista?(S/N) '))
        if resp not in 'Ss':
            break
    print(f'Você adicionou {len(lista)} dígitos na lista.')
    lista.sort(reverse=True)
    print(f'A lista em ordem decrescente é: {lista}')
    if 5 in lista:
        print('O valor 5 foi digitado, portanto, está na lista.')
    else:
        print('O valor 5 não foi digitado, portanto, não está na lista.')
else:
    print('Certo, tenha um bom dia!')