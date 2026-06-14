def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            m = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return m


#Programa Principal
num = leiaInt('Digite um número inteiro:')
num2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {num} e o número real digitado foi {num2}')