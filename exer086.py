matriz = [[], [], []]
for numeros in range(3):
    valor = int(input(f'Digite um valor para a [0, {numeros}]: '))
    matriz[0].append(valor)
for numeros in range(3):
    valor = int(input(f'Digite um valor para a [1, {numeros}]: '))
    matriz[1].append(valor)
for numeros in range(3):
    valor = int(input(f'Digite um valor para a [2, {numeros}]: '))
    matriz[2].append(valor)
print('-=' * 30)
print(f'{matriz[0]}\n {matriz[1]}\n {matriz[2]}')
