from time import sleep


def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    sleep(0.5)
    for numeros in range(1, 11):
        print(numeros, end=' ', flush=True)
        sleep(0.1)
    print('FIM!')

    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for numeros in range(10, 0 - 1, -2):
        print(numeros, end=' ', flush=True)
        sleep(0.1)
    print('FIM!')
    print('-=' * 20)

    print('Agora é a sua voez de personalizar a contagem!')
    start = int(input('Início: '))
    stop = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-=' * 20)

    for numeros in range(start, stop - 1, passo):
        print(numeros, end=' ', flush=True)
        sleep(0.1)
    print('FIM!')


contador()
