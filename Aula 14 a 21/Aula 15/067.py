cont = 1

while True:
    num = int(input('\nEscolha um número e veja sua tabuada [(-2) para parar]: '))
    if num < 0:
        print('Programa de Tabuada Encerrado. Volte Sempre.')
        break
    while True:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
        if cont == 11:
            cont - 11
            break
