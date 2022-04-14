valor = list()

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

count = len(valor)
print(f'Foram digitados {count} valores')

valor.sort(reverse=True)
print(f'Você digitou os valores {valor}')

if 5 in valor:
    print('O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')