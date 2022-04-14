
from time import sleep

pergunta = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número número: '))

while pergunta != 5:
    pergunta = int(input('''\nVocê quer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    : '''))

    if pergunta == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif pergunta == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif pergunta == 3:
        if  n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif pergunta == 4:
        n1 = int(input('\nDigite um número: '))
        n2 = int(input('Digite outro número número: '))
    elif pergunta > 5 or pergunta < 1:
        print('Opção invalida.')
    else:
        print('Finalizando...')
        sleep(1.5)
        