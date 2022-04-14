from random import randrange
from time import sleep

print(f'''{'-' * 14}
 PAR OU IMPAR
{'-'*14}''')

cont = 0

while True:
    pc = randrange(1, 11)
    jogada = int(input('\nDigite um valor: '))
    pi = str(input('Você quer par ou ímpar [P/I]? ')).upper().strip()[0]
    s = (jogada + pc) % 2

    if pi == 'P' and s == 0:
        print(f'\nVocê jogou {jogada} e o pc {pc}. Total deu {jogada + pc}, Deu PAR ')
        print('Você venceu.')
        print('Vamo jogar novamente...')     
        sleep(1.5)

    elif pi == 'I' and s == 0:
        print(f'\nVocê jogou {jogada} e o pc {pc}. Total deu {jogada + pc}, Deu PAR ')
        print('Você perdeu.')
        break
    
    elif pi == 'P' and s == 1:
        print(f'\nVocê jogou {jogada} e o pc {pc}. Total deu {jogada + pc}, Deu Impar')
        print('Você perdeu.')
        break

    elif pi == 'I' and s == 1:
        print(f'\nVocê jogou {jogada} e o pc {pc}. Total deu {jogada + pc}, Deu Impar')
        print('Você venceu.')
        print('Vamo jogar novamente...')     
        sleep(1.5)

    cont += 1
print(f'\nVocê venceu {cont} vezes seguidas')


