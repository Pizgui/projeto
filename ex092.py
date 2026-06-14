from datetime import datetime
anoat = datetime.now().year
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
anonas = int(input('Ano de nascimento: '))
cadastro['Idade'] = (anoat- anonas)
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in cadastro.items():
    print(f'{k} tem o valor: {v}')