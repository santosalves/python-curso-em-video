sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
if (sexo == 'M') or (sexo == 'F'):
    print('Sexo {} registrado com sucesso.'.format(sexo))
else:
    while (sexo != 'M') and (sexo != 'F'):
        sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
    print('Sexo {} registrado com sucesso.'.format(sexo))
