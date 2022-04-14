escolha = tent = soma = 0
escolha = int(input('Número [999 para parar]: '))

while escolha != 999:
    soma += escolha
    tent += 1
    escolha = int(input('Número [999 para parar]: '))
print(f'Você tentou {tent} vezes. A soma entre eles é {soma}')
