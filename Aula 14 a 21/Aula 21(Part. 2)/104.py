def leiaInt(num):
    num = input('Digite um número: ')
    if num.isnumeric():
       return num
    else:
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        while True:
            num = input('Digite um número: ')
            if num.isnumeric():
                return num
                break
            else:
                print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
