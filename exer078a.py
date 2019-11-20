lista = []
for posicao in range(5):
    valor = int(input(f'Digite um valor para a posição {posicao}: '))
    lista.append(valor)

print('-=' * 20)
print(f'Você digitou os valores: {lista}')
maior = max(lista)
menor = min(lista)

print(f'O maior valor foi {maior} na posição ', end='')
for indice, num in enumerate(lista):
    if num == maior:
        print(f'{indice}...', end='')

print(f'\nO menor valor foi {menor} na posição ', end='')
for indice, num in enumerate(lista):
    if num == menor:
        print(f'{indice}...', end='')
