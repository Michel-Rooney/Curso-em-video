from random import randrange

secreto = randrange(1, 11)
verdadeiro = True
tentativas = 1

while verdadeiro:
    numero = int(input('\nTente acerta o número que estou pensando de [1 à 10]: '))
    if numero == secreto:
        print(f'Você acertou em {tentativas} tentativas')
        verdadeiro = False
    else:
        if secreto > numero:
            print('Mais... Tente Novamente')
        else:
            print('Menos... Tente Novamente')
    tentativas += 1
    