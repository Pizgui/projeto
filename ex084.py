temp = []
perm = []
resp = 's'
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(perm) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    perm.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar?(S/N) '))
    if resp in 'Nn':
        break
print(f'Os dados foram: {perm}')
print(f'Você cadastrou ao todo: {len(perm)} pessoas. ')
print(f'O maior peso foi de {mai}Kg')
for p in perm:
    if p[1] == mai:
        print(f'As pessoas com o maior peso são: {p[0]}')
print(f'O menor peso foi de {men}Kg')
for p in perm:
    if p[1] == men:
        print(f'As pessoas com o menor peso são: {p[0]}')