homens = mulheres = total_pessoas = 0
while True:
    print('-' * 30)
    print('Cadastre uma Pessoa')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]:')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    if idade >= 18:
       total_pessoas += 1
    escolha = str(input('Quer continuar?[S/N]:')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total_pessoas}')
print(f'Ao todo temos {homens} homen(s) cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
