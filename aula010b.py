n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('=' * 20)
print('A sua média foi {:.1f}'.format(m))
print('=' * 20)
if m >= 7.0:
    print('Você está aprovado!!')
else:
    print('Você está repovado!!')
print('=' * 20)
