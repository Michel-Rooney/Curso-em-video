def escreva(txt):
    tam = len(txt) + 2
    print('-' * tam)
    print(f' {txt}')
    print('-' * tam)

digite = str(input('Digite algo: '))
escreva(digite)