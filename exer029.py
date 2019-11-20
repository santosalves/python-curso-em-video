v = float(input('Qual a velocidade do veículo?: '))
m = (v - 80) * 7.00
if v > 80:
    print('Você excedeu o limite e não poderá passar. Multa de R$: {} reais'.format(m))
else:
    print('Você está dentro do limite!'.format(v))
print('Tenha um bom dia, dirija com segurança!')
