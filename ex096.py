def calcular(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m².')


print('Controle de Terrenos')
print('-' * 20)
a = int(input('LARGURA (m): '))
b = int(input('COMPRIMENTO (m): '))
calcular(a, b)