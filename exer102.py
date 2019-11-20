def fatorial(num, show=False):
    """
    Além do número para cáculcular o fatorial, podemos passar
    como parâmetro opcional os valores: True ou False.

    Por padrão, o valor é False.
    Isso quer dizer que será mostrado somente o resultado final.

    Se o valor True for passado como segundo parâmetro,
    a saída será mostrada no formato de conta.

    Ex com parâmetro :
        print(fatorial(5, True))
        5 x 4 x 3 x 2 x 1 = 120
    """

    from time import sleep
    resultado = num
    if show is True:
        for contador in range(num, 0, - 1):
            if contador != 1:
                print(f'{contador} x ', end='', flush=True)
                resultado *= (contador - 1)
                sleep(0.4)
            elif contador == 1:
                print(f'{contador} = ', end='')
                return resultado
    elif show is False:
        for contador in range(num, 0, - 1):
            if contador == 1:
                break
            resultado *= (contador - 1)
        return resultado


print('-' * 26)
print(fatorial(5, True))
