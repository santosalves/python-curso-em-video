fatorial = int(input('''Digite um numero para
calular o Fatorial: '''))
num = fatorial
resultado = 1
print('Calcule {}! = '.format(num), end='')
while fatorial > 0:
    resultado = fatorial * resultado
    if fatorial > 1:
        print('{} x '.format(fatorial), end='')
    elif fatorial == 1:
        print('{} = '.format(fatorial), end='')
    fatorial -= 1
print(resultado)
