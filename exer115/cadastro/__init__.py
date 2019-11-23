def ver_cadastro():
    print('-' * 50)
    print('OPÇÃO 1'.center(50))
    print('-' * 50)

    try:
        arquivo = open('cursoemvideo.txt', mode='rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]} anos')
    finally:
        arquivo.close()


def cadastrar_pessoas(arq, nome='desconhecido', idade=0):
    print('-' * 50)
    print('OPÇÃO 2'.center(50))
    print('-' * 50)

    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print('Novo registro adicionado')


def sair():
    print('-' * 50)
    print('Saindo do sistema... Até logo!'.center(50))
    print('-' * 50)


def criar_arquivo():
    try:
        arq = open('cursoemvideo.txt', mode='r')
    except FileNotFoundError:
        arq = open('cursoemvideo.txt', mode='w')
        print('Arquivo cursoemvideo.txt criado com sucesso!')
    finally:
        arq.close()
