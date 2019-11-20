from random import randint
from time import sleep


def sorteando(lista):
    num_sorteio = randint(1, 10)
    print(f'Sorteando {num_sorteio} valores da lista: ', end='', flush=True)
    for qtd_numeros in range(num_sorteio):
        num_random = randint(1, 10)
        print(num_random, end=' ', flush=True)
        sleep(0.5)
        lista.append(num_random)
    print('PRONTO!')


def soma():
    somatorio = 0
    for elemento in lista:
        if elemento % 2 == 0:
            somatorio += elemento
    print(f'Somando os valores pares de {lista}, temos {somatorio}')


lista = []
sorteando(lista)
soma()
