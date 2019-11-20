cadastro = []
seclista = []
maior = menor = 0
while True:
    seclista.append(str(input('Nome: ').strip()))
    seclista.append(str(input('Peso: ').strip()))

    if len(cadastro) == 0:
        maior = menor = seclista[1]
    else:
        if seclista[1] > maior:
            maior = seclista[1]
        if seclista[1] < menor:
            menor = seclista[1]

    cadastro.append(seclista[:])
    seclista.clear()
    avance = input('Quer continuar[S/N]?: ').upper().strip()

    if avance == 'S':
        continue
    elif avance == 'N':
        break
    else:
        continue

print('-=' * 25)
print(f'Ao todo você cadastrou {len(cadastro)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoas in cadastro:
    if pessoas[1] == maior:
        print(f'[{pessoas[0]}]', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for pessoas in cadastro:
    if pessoas[1] == menor:
        print(f'[{pessoas[0]}]', end='')
