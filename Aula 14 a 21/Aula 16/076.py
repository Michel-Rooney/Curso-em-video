#list = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

#print(f'''{'-' * 40}
#          LISTAGEM DE PREÇOS     
#{'-' * 40}''')

#print(f'''{list[0]}...................... R$  {list[1]}
#{list[2]}................... R$  {list[3]}
#{list[4]}.................... R$  {list[5]}
#{list[6]}..................... R$  {list[7]}
#{list[8]}............... R$  {list[9]}
#{list[10]}................... R$  {list[11]}
#{list[12]}.................... R$  {list[13]}
#{list[14]}.................... R$  {list[15]}
#{list[16]}...................... R$  {list[17]}''')

list = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'R${list[pos]:>7.2f}')
print('-' * 40)
