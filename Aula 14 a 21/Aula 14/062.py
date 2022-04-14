print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
n1 = 10

mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('FIM')
    mais = int(input('Quantos números a mais você quer?: '))
print(f'Progresão terminada com {total} termos mostrados')
