num = int(input('Escolha um número inteiro: '))
print ('''Escolha uma das bases para a conversão:'
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para binário é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexaecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')