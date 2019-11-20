from random import randint

tupla = ()
print('Os valores sorteador foram: ', end=' ')
for contador in range(5):
    aleatorio = randint(0, 20)
    print('{}'.format(aleatorio), end=' ')
    tupla += (aleatorio,)
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
