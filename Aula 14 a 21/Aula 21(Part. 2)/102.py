def fatorial(n, show=False):
    """Calcular o fatorial de um número

    Args:
        n: O número para ser calculador
        show (bool, optional): Mostra ou não o calculo. Defaults to False.

    Returns: O valor do fatorial de n.
    """

    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


valor = int(input('Digite um número: '))
ver = str(input('Deseja ver o calculo [S/N]: '))
if ver in 'Ss':
    verdadeiro = True
else:
    verdadeiro = False
print(fatorial(valor, verdadeiro))
ver2 = str(input('\nDeseja ver a docstring de fatorial()? [S/N]:'))
if ver2 in 'Ss':
    help(fatorial)
