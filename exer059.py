from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
ops = 0
while ops != 5:
    print('[1]SOMA\n'
          '[2]MULTIPLICAÇÃO\n'
          '[3]MAIOR\n'
          '[4]NOVOS NÚMEROS\n'
          '[5]SAIR DO PROGRAMA\n')
    ops = int(input('Escolha uma opção: '))
    if ops == 1:
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, primeiro + segundo))
        print('=' * 25)
        sleep(2)
    elif ops == 2:
        print('A multiplicação entre {} X {} é {}'.format(primeiro, segundo, primeiro * segundo))
        print('=' * 15)
        sleep(2)
    elif ops == 3:
        if primeiro > segundo:
            print('Entre {} e {}, o maior valor é {}'.format(primeiro, segundo, primeiro))
            print('=' * 25)
            sleep(2)
        else:
            print('Entre {} e {}, o maior valor é {}'.format(primeiro, segundo, segundo))
            print('=' * 25)
            sleep(2)
    elif ops == 4:
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
        sleep(2)
    elif ops == 5:
        print('Finalizando...')
        print('=' * 25)
        sleep(2)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida. Tente novamente!')
        print('=' * 25)
        sleep(2)
