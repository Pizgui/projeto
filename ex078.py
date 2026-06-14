lista = []
mai = 0
men = 0
for c in range (0,5):
    lista.append(int(input('Digite um valor numérico: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi: {mai} e está na posição ', end='')
for i, v in enumerate(lista):
    if lista[i] == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi: {men} e está na posição ', end='')
for i, v in enumerate(lista):
    if lista[i] == men:
        print(f'{i}...', end ='')
print()