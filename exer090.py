aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 30)

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for key, value in aluno.items():
    print(f' - {key} é igual a {value}')
