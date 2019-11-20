print('Gerador de PA')
print('=-' * 20)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

contador = 1
progress = termo1

print(termo1, '> ', end="")
while contador < 10:
    contador += 1
    progress += razao
    print(progress, '> ', end="")
    if contador == 10:
        print('FIM!')
