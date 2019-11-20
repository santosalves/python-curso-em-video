matriz = [[], [], []]
soma = coluna3 = maior = 0
for numeros in range(3):
    valor = int(input(f'Digite um valor para a [0, {numeros}]: '))
    if valor % 2 == 0:
        soma += valor
    matriz[0].append(valor)
    if numeros == 2:
        coluna3 += valor
for numeros in range(3):
    valor = int(input(f'Digite um valor para a [1, {numeros}]: '))
    if valor % 2 == 0:
        soma += valor
    matriz[1].append(valor)
    if numeros == 2:
        coluna3 += valor
    if maior <= valor:
        maior = valor
for numeros in range(3):
    valor = int(input(f'Digite um valor para a [2, {numeros}]: '))
    if valor % 2 == 0:
        soma += valor
    matriz[2].append(valor)
    if numeros == 2:
        coluna3 += valor
print('-=' * 30)
print(f'{matriz[0]}\n {matriz[1]}\n {matriz[2]}')
print('-=' * 30)

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior valor da segunda linha é {maior}.')
