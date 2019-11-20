#O valor do alugue do carro por dia é de R$: 60,00
#O valor por Km é R$: 0,15

dias = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Quantos Km foram percorridos?: '))
pago = (dias * 60) + (km * 0.15)

print('O total a pagar é {:.2f}'.format(pago))
