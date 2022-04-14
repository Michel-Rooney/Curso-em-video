
valor = valor2 = valor3 = list()
cont = cont2 = n1 = 0


while True:
    num = int(input("\nDigite um valor: "))
    if num not in valor:
        valor.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor já existe. Não irei adicionar')

    while True:
        continuar = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        else:
            pass 
    
    if continuar == 'S':
        pass
    else:
        break

print(valor)

print(f'Lista com núemros pares: ', end='')
for num in valor:
    if num % 2 == 0:
       print(num, end = ' ')

print(f'\nLista com núemros ímpares: ', end='')
for num in valor:
    if num % 2 == 1:
        print(num, end=' ')




