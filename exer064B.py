num = 0
contador = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    contador += 1
    soma += num
print('Você digitou {} numeros e a soma entre eles é {}.'.format(contador, soma))
