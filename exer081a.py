lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    continuar = str(input('Quer continuar[S/N]?: ')).upper().strip()
    if continuar == 'N':
        break
print(f'Foram digitados {len(lista)} elementos')

lista.sort(reverse=True)
print(f'A lista na ordem decrescente é {lista}')

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
