from datetime import date
pessoa = dict()

agora = date.today()
agora = agora.year

pessoa['nome'] = str(input('Seu nome: '))
pessoa['Ano de nascimento'] = int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Sálario'] = float(input('Sálario: '))

    print('\nSeu nome é {}'.format(pessoa['nome']))
    print('Tem {} anos de idade'.format(agora - pessoa['Ano de nascimento']))
    print('CTPS: {}'.format(pessoa['CTPS']))
    print('Você foi contratado em {}'.format(pessoa['Contratação']))
    print('Seu sálario é de {}'.format(pessoa['Sálario']))
    print('Você vai se aposentar daqui {} anos (levando em cosideração a aposentadoria de 35)'.format((pessoa['Contratação'] + 35) - agora))

else:
    print('\nSeu nome é {}'.format(pessoa['nome']))
    print('Tem {} de idade'.format(agora - pessoa['Ano de nascimento']))
    print('CTPS: {}'.format(pessoa['CTPS']))

