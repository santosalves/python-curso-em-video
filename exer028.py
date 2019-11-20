from random import randint
from time import sleep
qa = randint(0, 5) #Faz o computador pensar - qa significa: 'Qualquer Aleatório'
print('-=-' * 20)
print('Vou pensar em um número de 0 à 5. Tente adivinhar..')
print('-=-' * 20)
n = int((input('Que número eu pensei?: '))) #O jogador tenta adivinhar
print('Processando...')
sleep(1)
if n == qa:
    print('Você venceu!')
else:
    print('Você Perdeu!, pensei no {}'.format(qa))
