


while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        print('Você é do sexo masculino.')
        break
    elif sexo == 'F':
        print('Você é do sexo feminino.')
        break
    else:
        print('Esse sexo não existe. Digite novamente')
        


# sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Sexo inválido. Digite novamente [M/F]: ')).strip().upper()[0]
# print(f'Sexo {sexo} registrado com sucesso.')
