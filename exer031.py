dis = float(input('Qual a distância da sua viagem?: '))
if dis > 200:
    print('A sua viagem promocional de {}km sairá por R$: {} reais'.format(dis, dis * 0.45))
else:
    print('A sua viagem de {}km sairá por R$: {} reais'.format(dis, dis * 0.50))
