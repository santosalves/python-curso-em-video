p = float(input('Qual é o preço do produto?: R$'))
desc = p - (p * 5 / 100)
print('O preço é R$: {:.2f} reais, mas à vista faço por R$: {:.2f} reais, com 5% de desconto'.format(p, desc))
