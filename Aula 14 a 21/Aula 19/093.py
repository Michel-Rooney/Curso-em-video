perfil = dict()
lista = list()
total = 0

perfil['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas?: '))

for i in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {i+1}: '))
    lista.append(gols)
perfil['gols'] = lista[:]

for i in lista:
    total += i
perfil['total'] = total

print('=-'* 30)
print(perfil)
print('=-'* 30)
print('O campo nome tem o valor: {}'.format(perfil['nome']))
print('O campo gols tem o valor: {}'.format(perfil['gols']))
print('O campo total tem o valor: {}'. format(perfil['total']))
print('=-'* 30)
print('O jogador {} jogou {} partidas'.format(perfil['nome'], partidas))

for i, g in enumerate(perfil['gols']):
    print(f'    => Na partida {i+1}, fez {g} gols.')
print('Foi um total de {} gols'.format(perfil['total']))