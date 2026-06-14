def aumentar(num, por, form=False):
    total = num + (num * por/100)
    return total


def diminuir(num, por, form=False):
    total = num - (num * por / 100)
    return total

def dobro(num, form=False):
    total = num * 2
    return total


def metade(num, form=False):
    total = num /2
    return total


def moeda(valor):
    valor = (f'R${valor}')
    return valor