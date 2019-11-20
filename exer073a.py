times = ('Flamengo', 'São Paulo', 'Sport', 'Palmeiras', 'Atlético-MG',
         'Cruzeiro', 'Corinthians', 'Internacional', 'Vasco', 'Fluminense',
         'América-MG', 'Botafogo', 'Chapecoense', 'Vitória', 'Santos',
         'Atlético-PR', 'Paraná', 'Bahia', 'Ceará')

print('-=' * 30)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 30)

print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 30)


print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 30)

print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)

print(f'O {times[12]} está na posição {times.index("Chapecoense") + 1}ª posição')
