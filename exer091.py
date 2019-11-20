from time import sleep
from random import randint
from operator import itemgetter

dado = {}
ranking = list()
print('Valores sorteados: ')
for valores in range(1, 5):
    dado['jogador' + str(valores)] = randint(1, 7)

for chave, valor in dado.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(0.7)
print('-=' * 30)

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print(' == RANKING DOS JOGADORES == ')
for indice, valor in enumerate(ranking):
    print(f'{indice + 1} lugar: {valor[0]} com {valor[1]}.')
    sleep(0.7)



