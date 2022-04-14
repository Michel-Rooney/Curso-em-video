def metade(n=0):
    n2 = n / 2
    return n2


def dobro(n=0):
    n2 = n * 2
    return n2


def aumentar(n=0, p=0):
    n2 = ((n / 100) * p) + n
    return n2 


def diminuir(n=0, p=0):
    n2 = n - ((n / 100) * p)
    return n2


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')