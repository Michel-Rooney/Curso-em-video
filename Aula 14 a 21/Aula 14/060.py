from math import factorial
numero = int(input('Digite um número e descubra seu fatorial: '))
print(factorial(numero))


n = int(input('Digite um número para calcular seu fatorial: '))
c = n 
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
	print(f'{c}', end='')
	print(' x ' if c > 1 else ' = ', end='')
	f *= c
	c -= 1
print(f'{f}')