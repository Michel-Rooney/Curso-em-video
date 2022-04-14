def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def dobro(preço=0, taxa=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')