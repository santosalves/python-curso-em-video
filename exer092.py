from datetime import datetime

funcionário = dict()
funcionário['Nome'] = str(input('Nome: ')).capitalize().strip()
funcionário['Nascimento'] = int(input('Ano de Nascimento: '))
funcionário['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))

idade = datetime.now().year
if funcionário['CTPS'] == 0:
    print(f' - nome tem o valor {funcionário["Nome"]}')
    print(f' - idade tem o valor {idade - funcionário["Nascimento"]}')
    print(f' - ctps tem o valor {funcionário["CTPS"]}')
else:
    funcionário['Contratação'] = int(input('Ano de contratação: '))
    funcionário['Salário'] = float(input('Salário: '))

print('-=' * 30)

print(f' - nome tem o valor {funcionário["Nome"]}')
print(f' - idade tem o valor {idade - funcionário["Nascimento"]}')
print(f' - ctps tem o valor {funcionário["CTPS"]}')
print(f' - contratação tem o valor {funcionário["Contratação"]}')
print(f' - Salário tem o valor {funcionário["Salário"]}')
print(f' - aposentadoria tem o valor {70 - (idade - funcionário["Nascimento"])}')
