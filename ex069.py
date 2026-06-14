maioridade = fmvinte = homens = total = 0
opc = ''
while True:
    print('-'*50)
    sexo = str(input('Qual o sexo de pessoa sendo cadastrada? [F/M] '))
    while sexo not in 'FfMm':
        sexo = str(input('Qual o sexo de pessoa sendo cadastrando? [F/M] '))
    idade = int(input('Qual a idade da pessoa sendo cadastrada? '))
    total += 1
    if idade > 17:
        maioridade += 1
    if sexo in 'Ff'and idade < 20:
            fmvinte += 1
    else:
        homens += 1
    opc = str(input('Deseja cadastrar mais uma pessoa? [S/N]'))
    while opc not in 'SsNn':
        opc = str(input('Deseja cadastrar mais uma pessoa? [S/N]'))
    if opc in 'Nn':
        break
print('=-'*25)
print(f'''Dados das pessaos registradas: 
Total de cadastros - {total}
Maiores de 18 anos - {maioridade}
Mulheres com menos de 20 anos - {fmvinte}
Homens - {homens}''')