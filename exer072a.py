tupla = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Erro, tente novamente.')
        continue
    print(f'Você digitou o número {tupla[num]}')
    print('=' * 20)

    while True:
        continuar = input('Você deseja continuar [S/N]?: ').upper()
        if continuar == 'S':
            print('OK...\n')
            break
        elif continuar == 'N':
            break
        else:
            print('=' * 20)
            print('Opção inválida. Tente novamente.')
            continue

    if continuar == 'N': #Só irá encerrar após um break em cada laço
        break
