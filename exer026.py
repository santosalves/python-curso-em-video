frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira posição da letra A, é: {}'.format(frase.find('A') + 1))
print('A última posição do A é: {}'.format(frase.rfind('A') + 1))
