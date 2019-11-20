jogadores = dict()
jogadores['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
npartidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou: '))

ngols = []
for partidas in range(npartidas):
    ngols.append(int(input(f'    Quantos gols na partida {partidas}?: ')))
jogadores['gols'] = ngols[:]

soma_gols = 0
for gols in ngols:
    soma_gols += gols
jogadores['total'] = soma_gols

print('-=' * 30)
print(jogadores)
print('-=' * 30)
print(f'O campo nome tem o valor {jogadores["nome"]}')
print(f'O campo gols tem o valor {jogadores["gols"]}')
print(f'O campo total tem o valor {jogadores["total"]}')
print('-=' * 30)

print(f'O jogador {jogadores["nome"]} jogou {npartidas} partidas.')
for partidas in range(npartidas):
    print(f'    => Na partida {partidas}, fez {ngols[partidas]} gols.')
print(f'Foi um total de {jogadores["total"]} gols.')

print('-=' * 30)





