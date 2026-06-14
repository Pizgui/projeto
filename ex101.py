from datetime import datetime
def voto(num):
    idade = datetime.now().year - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif idade in (16,17,18) or idade > 64:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade > 18 and idade <65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


print('-'*20)
ano = int(input('Em que ano você nasceu? '))
voto(ano)