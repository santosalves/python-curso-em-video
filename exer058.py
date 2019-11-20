from random import randint
from time import sleep

print('=-' * 8, 'Sou o seu computador...', '=-' * 8)
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1.2)
print('Será que você consegue adivinhar qual foi?')
sleep(1)
print('=-' * 28)
computador = randint(0, 10)
tentativas = 1
palpite = int(input('Qual é o seu palpite: '))
print('=-' * 28)
if palpite == computador:
    print('Você acertou de primeira. Parabéns!')
else:
    while palpite != computador:
        tentativas += 1
        if palpite < computador:
            print('Mais... Tente mais uma vez.')
            sleep(1)
            palpite = int(input('Qual é o seu palpite: '))
            print('=-' * 28)
        else:
            print('Menos... Tente mais uma vez.')
            sleep(1)
            palpite = int(input('Qual é o seu palpite: '))
            print('=-' * 28)
    print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
