escola = {}
escola['nome'] = str(input('Nome: '))
escola['media'] = float(input(f'Média do {escola["nome"]}: '))
if escola['media'] > 6:
    escola['situacao'] = 'Aprovado'
else:
    escola['situacao'] = 'Reprovado'
print(f'Nome é igual a: {escola["nome"]}')
print(f'Média é igual a: {escola["media"]}')
print(f'Situação é igual a: {escola["situacao"]}')