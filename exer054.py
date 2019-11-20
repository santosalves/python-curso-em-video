from datetime import date

ano_atual = date.today().year
menor = 0
maior = 0

for contador in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu?: '.format(contador)))
    if (ano_atual - nascimento) < 21 and (ano_atual - nascimento > 0):
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} maiores de idade.'.format(maior))
print('Também tivemos {} pessoas menores de idade.'.format(menor))
