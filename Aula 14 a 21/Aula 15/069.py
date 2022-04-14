maior = homem = mue = 0
while True:
    print(f'''{'-'*23}
  CADASTRE UMA PESSOA  
{'-'*23}''')
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mue += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nDeseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'S':
        nada = 1
    else:
        break
print('\n=== FIM DO PROGRAMA ===')
print(f'Total de pessoas com mais de 18: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mue} mulheres com menos de 20')