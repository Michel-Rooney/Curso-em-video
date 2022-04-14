estudante = dict()

estudante['Aluno'] = str(input('Nome: '))
estudante['Media'] = float(input(f'Média de {estudante["Aluno"]}: '))

if estudante['Media'] >= 7.0:
    print(f'{estudante["Aluno"]} foi aprovado')
elif estudante['Media'] >= 5.0:
    print(f'{estudante["Aluno"]} esta de recuperação')
else:
    print(f'{estudante["Aluno"]} foi reprovado')