from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('\nAnalisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}.')


#Programa Principal
maior()