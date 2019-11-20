from random import randint
from time import sleep

print('-' * 50)
print('             JOGA NA MEGA SENA             ')
print('-' * 50)

n_jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print('-' * 3, f' SORTEANDO {n_jogos} JOGO(S) ', '-' * 3)
for jogos in range(n_jogos):
    numeros = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    set(numeros)
    list(numeros)
    if len(numeros) != 6:
        while len(numeros) != 6:
            novo_número = randint(1, 60)
            if novo_número not in numeros:
                numeros.append(novo_número)
    numeros.sort()
    print(f'Jogo {jogos + 1}: {numeros}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
