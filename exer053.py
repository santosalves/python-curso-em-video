frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

print('O inverso de {} é: {}'.format(junto, junto[::-1]))
if frase[::-1] == frase:
    print('Temos um PALÍNDROMO!')
else:
    print('Não é um PALÍNDROMO!')
