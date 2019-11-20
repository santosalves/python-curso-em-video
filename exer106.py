from time import sleep


def sistema():
    while True:
        msg = 'SISTEMA DE AJUDA PyHelp'
        print('\033[1;102m~' * (len(msg) + 4))
        print(f'  {msg}')
        print('~' * (len(msg) + 4))

        item = str(input('\033[0;0mFunção ou Biblioteca > ')).strip().lower()
        if item == 'fim':
            break

        comando = 'Acessando o manual do comando '
        print('\033[1;104m~' * (len(comando) + 4))
        print(f' {comando} "{item}"')
        print('~' * (len(comando) + 4))

        print('\033[1;107m', end='')
        sleep(1)
        help(item)


sistema()
msg = 'ATÉ LOGO!'
print('\033[1;41m~' * (len(msg) + 4))
print(f'  {msg}')
print('~' * (len(msg) + 4))
