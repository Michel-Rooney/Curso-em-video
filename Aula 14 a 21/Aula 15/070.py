print(f'''{'-'*28}
     LOJA SUPER BARATÃO     
{'-'*28}''')
total = prod = pmb = 0
while True:
    produto = str(input('\nNome do Produto: '))
    preço = int(input('Preço R$'))
    total += preço
    if preço > 1000:
        prod += 1
    preço2 = 10000000000000000
    if preço <= preço2:
        nome = produto
        valor = preço
        preço2 = preço
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nDeseja continuar [S/N]? ')).upper().split()[0]
    if continuar == 'S':
        nada = 1
    else:
        break
print('\n-------- Fim do Programa --------')
print(f'O total da compra foi R${total}')
print(f'Temos {prod} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${valor}')
