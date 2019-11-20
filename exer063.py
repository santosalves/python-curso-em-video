print('-' * 25)
print('Sequência da FIBONACCI')
print('-' * 25)
termos = int(input('Quantos termos você quer mostrar?: '))
contador = 2
menor, maior = 0, 1
print('{} -> {} -> '.format(menor, maior), end='')
while contador < termos:
    contador += 1
    fibo = menor + maior
    print('{} -> '.format(fibo), end='')
    menor = maior
    maior = fibo
print('FIM!')
