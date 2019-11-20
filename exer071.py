print('=' * 50)
print('{:^50}'.format('BANCO CEV'))
print('=' * 50)
saque = int(input('Que valor você deseja sacar?: R$'))
contador_cinquenta = contador_vinte = contador_dez = contador_um = 0

while saque >= 50:
    saque -= 50
    contador_cinquenta += 1
if contador_cinquenta > 0:
    print(f'Total de {contador_cinquenta} células de R$50')

while saque >= 20:
    saque -= 20
    contador_vinte += 1
if contador_vinte > 0:
    print(f'Total de {contador_vinte} células de R$20')

while saque >= 10:
    saque -= 10
    contador_dez += 1
if contador_dez > 0:
    print(f'Total de {contador_dez} células de R$10')

while saque >= 1:
    saque -= 1
    contador_um += 1
if contador_um > 0:
    print(f'Total de {contador_um} células de R$1')

print('=' * 50)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
