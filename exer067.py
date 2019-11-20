while True:
    tabuada = int(input('Quer ver a tabuada de qual valor?: '))
    print('-=' * 25)
    if tabuada < 0:
        break
    for contador in range(1, 11):
        print(f'{tabuada} X {contador:2} = {tabuada * contador:2}')
    print('-=' * 25)
print('Programa de tabuada encerrado. Volte sempre!')
