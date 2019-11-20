lista = []

while True:
    valor = int(input('Digite um valor: '))

    if valor in lista:
        print('Valor duplicado! Não irei adicionar...')
    elif valor not in lista:
        lista.append(valor)
        print('Adicionado com sucesso...')

    continuar = str(input('Quer continuar?: ')).upper().strip()
    print('-=' * 20)
    if continuar == 'N':
        break
lista = sorted(lista)
print(f'Você digitou os valores {lista}')
