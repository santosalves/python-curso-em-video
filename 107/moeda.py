def aumentar(preço, percent):
    extra = preço * percent / 100
    preço += extra
    return preço


def diminuir(preço, percent):
    extra = preço * percent / 100
    preço -= extra
    return preço


def dobro(preço):
    return preço * 2


def metade(preço):
    return preço / 2
