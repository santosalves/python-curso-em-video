print('{:-^40}'.format('Loja Super Baratão'))
total = mais_de_mil = contador = 0
while True:
    produto = str(input('Nome do produto: ')).upper()
    preço = float(input('Preço: R$'))
    contador += 1
    total += preço

    if contador == 1 or preço_barato >= preço:
        preço_barato = preço
        produto_barato = produto
    if preço >= 1000:
        mais_de_mil += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais_de_mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {produto_barato} que custa R${preço_barato:.2f}')
