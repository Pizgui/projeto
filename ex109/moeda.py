def aumentar(num, por, form=False):
    total = num + (num * por/100)
    if form:
        return moeda(total)
    else:
        return total


def diminuir(num, por, form=False):
    total = num - (num * por / 100)
    if form:
        return moeda(total)
    else:
        return total

def dobro(num, form=False):
    total = num * 2
    if form:
        return moeda(total)
    else:
        return total


def metade(num, form=False):
    total = num /2
    if form:
        return moeda(total)
    else:
        return total


def moeda(valor):
    valor = (f'R${valor}')
    return valor