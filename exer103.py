def ficha(nome_jogador='<desconhecido>', gols=0):
    print(f'O jogador {nome_jogador} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
n_gols = str(input('Número de Gols: '))

if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0

if nome == '':
    print(ficha(gols=n_gols))
elif n_gols == str:
    print(ficha(nome_jogador=nome))
else:
    print(ficha(nome, n_gols))
