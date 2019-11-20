soma = 0
media = 0
total_mulheres = 0
nome_maisvelho = " "
for contador in range(1, 5):
    print('=========={}ª Pessoa =========='.format(contador))
    nome = str(input('Qual é o seu nome: '))
    idade = int(input('Qual é a sua idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma += idade
    if contador == 1:
        mais_velho = idade
    if (sexo == 'M') and (mais_velho < idade):
            mais_velho = idade
            nome_maisvelho = nome
    elif (sexo == 'F') and (idade < 20):
            total_mulheres += 1
    else:
        mais_velho = 0
        nome_maisvelho = 'Ninguém'
media = soma / contador
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(mais_velho, nome_maisvelho))
print('Ao todo são {} mulhere(s) com menos de 20 anos'.format(total_mulheres))
