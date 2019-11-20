from random import randint
from time import sleep

itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0, 2)

print('''Escolha:
      [0] Pedra
      [1] Papel
      [2]Tesoura''')
jogador = int(input("Qual é a sua escolha: "))

print("-=-" * 15)
print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO\n")
sleep(1)
print("-=-" * 15)
print("Você escolheu {} \nO computador escolheu {}".format(itens[jogador], itens[computador]))
print("-=-" * 15)

if computador == 0: #Coputador PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("O JOGADOR VENCE!")
    elif jogador == 2:
        print("O COMPUTADOR VENCE!")
elif computador == 1: #Coputador PAPEL
    if jogador == 0:
        print("O COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("O JOGADOR VENCE!")
elif computador == 2: #Coputador TESOURA
    if jogador == 0:
        print("O JOGADOR VENCE!")
    elif jogador == 1:
        print("O COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATE!")
