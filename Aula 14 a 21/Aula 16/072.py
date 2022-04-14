extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco",
    "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
    "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete",
    "Dezoito", "Dezenove", "Vinte")

while True:
    numero = int(input('Digite um número de [0 à 20]: '))
    if numero > 20 or numero < 0:
        print('Tente novamente.')
    else:
        print(f'Você digitou o número {extenso[numero]}')
        break
