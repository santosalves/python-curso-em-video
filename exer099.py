from time import sleep


def analise(* num):
    print('Analisando os valores passados...')
    sleep(1)
    for numeros in num:
        print(numeros, end=' ', flush=True)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(1)
    if len(num) == 0:
        print(f'O maior valor informado foi o 0.')
    else:
        print(f'O maior valor informado foi o {max(num)}.')
    print('-=' * 20)


print('-=' * 20)
analise(2, 9, 4, 5, 7, 1)
analise(4, 7, 0)
analise(1, 2)
analise(6)
analise()
