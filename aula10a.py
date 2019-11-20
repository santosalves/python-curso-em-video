nome = str(input('Qual é o seu nome?: ')).upper().strip()
if nome == 'PAULO':
    print('Que nome legal!')
else:
    print('Seu nome é tão normal..')
print('Bom dia, {}.'.format(nome))
