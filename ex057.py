s = input('Digite seu sexo (F/M): ').upper()
while s != 'M' and s != 'F':
    print('O valor digitado não é válido, tente novamente.\n')
    s = input('Digite seu sexo (F/M): ').upper()
if s == 'F':
    print('Muito obrigado, seu sexo é feminino.')
else:
    print('Muito obrigado, seu sexo é masculino.')