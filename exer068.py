from random import randint
from time import sleep

print('-=' * 28)
print('Vamos jogar PAR ou IMPAR')
print('-=' * 28)

contador = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    escolha_jogador = str(input('PAR ou IMPAR? [P/I]:')).upper()
    print('-' * 54)
    resultado = (jogador + computador) % 2
    if escolha_jogador == 'P' and resultado == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador}, DEU PAR.')
        print('-' * 54)
        contador += 1
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 28)
        sleep(1)
    elif escolha_jogador == 'P' and resultado == 1:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador}, DEU IMPAR.')
        print('VOCÊ PERDEU!')
        break
    elif escolha_jogador == 'I' and resultado == 1:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador}, DEU IMPAR.')
        print('-' * 54)
        contador += 1
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 28)
        sleep(1)
    elif escolha_jogador == 'I' and resultado == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador}, DEU PAR.')
        print('VOCÊ PERDEU!')
        break
print('-=' * 28)
print(f'GAME OVER! Voce ganhou {contador} veze(s)!')
