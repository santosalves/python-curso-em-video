contador = soma = maior = menor = 0
escolha = 'S'
executa = 'S'
while executa == 'S':
    if escolha == 'S':
        contador += 1
        num = int(input('Digite um número: '))
        soma += num
        if maior <= num: #Só irá atribuir se num for maior
            maior = num
        else: #Só executa quando num é menor que o valor da variável maior
            menor = num
        escolha = str(input('Quer continuar? [S/N]: ')).upper()
    elif escolha == 'N':
        media = soma / contador
        print('Você digitou {} números e a média foi {:.2f}'.format(contador, media))
        print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
        executa = 'N' #Acredito que um BREAK seja a melhor escolha para cancelar o laço. O BREAK ainda não foi ensinado.
    elif escolha != 'S' and escolha != 'N':
        print('Resposta incorreta. Tente novamente. ')
        escolha = str(input('Quer continuar? [S/N]: ')).upper()
        executa = 'S'
