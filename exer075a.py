tupla = ()

for contador in range(4):
    num = int(input('Digite um número: '))
    tupla += (num, )

print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição.')

print('Os valores pares digitados foram: ', end='')
for valores in tupla:
    if valores % 2 == 0:
        print(valores, end=' ')
