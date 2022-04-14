n = int(input('Digite um número e veja seu factorial: '))

f = 1

for i in range(1, n + 1):
    f *= i
    print(i, 'x ' if i < n else '= ', end='')
print(f)