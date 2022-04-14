def area(l, c):
    print(f'A área de um terreno {l} x {c} é de {l * c}m²')

print('\n--- CONTROLHE DE TERRENOS ---')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)
