from cadastro import *
from time import sleep


def menu():
    criar_arquivo()

    print('-' * 50)
    print('MENU PRINCIPAL'.center(50))
    print('-' * 50)

    print('\033[0:33m1 -\033[m \033[0:34mVer pessoas cadastradas\033[m'
          '\n\033[0:33m2 -\033[m \033[0:34mCadastrar nova Pessoa\033[m'
          '\n\033[0:33m3 -\033[m \033[0:34mSair do Sistema\033[m')

    print('-' * 30)
    while True:
        try:
            opção = int(input('\033[0:33mSua Opção:\033[m '))

            if opção == 1:
                ver_cadastro()
                menu()
            elif opção == 2:
                cadastrar_pessoas()
                menu()
            elif opção == 3:
                sair()
            else:
                print('\033[0:31mERRO!: Digite uma opção válida\033[m')
                sleep(2)
                menu()
        except ValueError:
            print('\033[0:31mERRO: por favor, digite um número válido')
            sleep(2)
            continue
        else:
            break
    print('-' * 30)

menu()
