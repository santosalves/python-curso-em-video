print('Gerador de PA')
print('=-' * 30)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 1
progress = termo1
print(termo1, '> ', end="")
while contador < 10:
    contador += 1
    progress += razao
    print(progress, '> ', end="")
    if contador == 10:
        print('PAUSA')

#Início da segunda contagem
mais_termos = int(input('Quantos termos você quer mostrar a mais?: '))
contador = 0 #É resetado para obdecer ao número de termos novos no While.
total_termos = mais_termos + 10 #Contagem dos termos mostrados
#Esse While só irá executar a quantidade de vezes correspondente ao número de termos digitados pelo usuário.
while contador < mais_termos:
    contador += 1
    progress += razao
    print(progress, '> ', end="")
    if contador == mais_termos:
        print('PAUSA')
        contador = 0 #Se não resetar o contador, o programa continua executando baseado no número anterior.
        mais_termos = int(input('Quantos termos você quer mostrar a mais?: '))
        total_termos += mais_termos
print('=-' * 30)
print('Progressão finalizada com {} termos mostrados.'.format(total_termos))
