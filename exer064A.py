num = contador = soma = 0
while num != 999:
    contador += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles é {}.'.format(contador, soma))
