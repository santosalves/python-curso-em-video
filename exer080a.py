lista = []
for contador in range(5):
    valor = int(input('Digite um valor: '))
    if contador == 0:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    elif valor < lista[contador - 1]:
        if contador == 4:
            menor = min(lista)
            if valor <= menor:
                lista.insert(0, valor)
                print('Adicionado na posição 0 da lista...')
            else:
                lista.insert(1, valor)
                print('Adicionado na posiçãoda 1 da lista...')
        else:
            lista.insert((contador - 1), valor)
            print(f'Adicionado na posição {contador - 1} da lista...')
    else:
        lista.append(valor)
        print('Adicionado ao final da lista...')

print(f'A lista ordenada é: {lista}')
