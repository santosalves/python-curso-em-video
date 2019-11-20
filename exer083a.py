expre = input('Digite um expressão: ')
aberto = expre.count('(')
fechado = expre.count(')')

if aberto == fechado:
    print('A sua expressão é válida')
else:
    print('A sua expressão é inválida')

