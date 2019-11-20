dados = dict()
lista_dados = list()
while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dados['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if dados['sexo'] == 'M' or dados['sexo'] == 'F':
            break
        print('ERRO! Responda apenas M ou F.')

    dados['idade'] = int(input('Idade: '))
    lista_dados.append(dados.copy())

    while True:
        continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(lista_dados)} pessoas cadastradas.')

# Fazendo a opção B
soma_idade = 0
for idade in lista_dados:
    soma_idade += idade['idade']
media = soma_idade / len(lista_dados)
print(f'B) A média de idade é de {media:.2f} anos.')
# FIM - B

# Fazendo a opção C
print(f'C) As mulheres cadastradas foram', end=' ')
for mulheres in lista_dados:
    if mulheres['sexo'] == 'F':
        print(f'{mulheres["nome"]}', end=' ')
print('')
# FIM - C

print('D) Lista das pessoas que estão acima da média:')
for acima_media in lista_dados:
    if acima_media['idade'] > media:
        print(f'    nome = {acima_media["nome"]};', end=' ')
        print(f'sexo = {acima_media["sexo"]};', end=' ')
        print(f'idade = {acima_media["idade"]};', end=' ')
        print('')
print('<< ENCERRADO >>')

