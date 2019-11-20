lista = 'LISTAGEM DE PREÇOS'
print('-' * 30)
print('{:^30}'.format(lista))
print('-' * 30)

tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
         'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.30, 'Livro', 34.90)

for itens in range(0, len(tupla), 2):
    print('{:.<20}R$ {:>6}'.format(tupla[itens], tupla[itens + 1]))


print('-' * 30)
