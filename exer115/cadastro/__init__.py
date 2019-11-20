def ver_cadastro():
    print('-' * 50)
    print('OPÇÃO 1'.center(50))
    print('-' * 50)

    with open('cursoemvideo.txt', mode='rt', encoding='utf-8') as arquivo:
        print(arquivo.read())
    arquivo.close()


def cadastrar_pessoas():
    print('-' * 50)
    print('OPÇÃO 2'.center(50))
    print('-' * 50)


def sair():
    print('-' * 50)
    print('Saindo do sistema... Até logo!'.center(50))
    print('-' * 50)


def criar_arquivo():
    try:
        arq = open('cursoemvideo.txt', mode='r')
    except FileNotFoundError:
        arq = open('cursoemvideo.txt', mode='w').close()
        arq.close()
        print('Arquivo cursoemvideo.txt criado com sucesso!')
    else:
        arq.close()
