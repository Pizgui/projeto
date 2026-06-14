lista = []
resp = 's'
while True:
    resp = str(input('Quer adicionar mais um número na lista?(S/N) '))
    if resp not in 'Ss':
        break
    else:
        num = int(input('Digite um número: '))
        if num not in lista:
            lista.append(num)
lista.sort()
print(lista)