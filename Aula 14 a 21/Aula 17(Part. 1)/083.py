# from itertools import count


# n1 = (str(input('Digite a expressão: ')))

# n2 = n1.count('(')
# n3 = n1.count(')')
# n4 = n2 + n3

# if n4 % 2 == 0:
#     print('A expressão está certa.')
# else:
#     print('Sua expressão está errada')


expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')