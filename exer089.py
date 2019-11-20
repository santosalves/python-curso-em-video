alunos = []
contador = 0

while True:
    nome = input('Nome: ')
    nota1 = input('Nota 1: ')
    nota2 = input('Nota 2: ')

    alunos.append([nome])
    alunos[contador].append(nota1)
    alunos[contador].append(nota2)
    contador += 1

    continuar = input('Quer continuar?[S/N]: ').strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
print('Nº Nome     Média')
print('-' * 30)

for posição in range(contador):
    if posição == 0:
        nota1 = float(alunos[posição][posição + 1])
        nota2 = float(alunos[posição][posição + 2])
        print(f'{posição}  {alunos[posição][posição]}     {(nota1 + nota2) / 2}')
    else:
        nota1 = float(alunos[posição][(posição - posição) + 1])
        nota2 = float(alunos[posição][(posição - posição) + 2])
        print(f'{posição}  {alunos[posição][posição - posição]}     {(nota1 + nota2) / 2}')
print('-' * 30)

notas_aluno = 0
while notas_aluno != 999:
    notas_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas_aluno == 999:
        break
    print(f'Notas de {alunos[notas_aluno][0]} são {alunos[notas_aluno][1:]}')
    print('-' * 30)

print('FINALIZANDO...')
print('<<<  VOLTE SEMPRE  >>>')
