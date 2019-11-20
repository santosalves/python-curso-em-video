soma = contador = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999: #O valor de parada se chama FLAG.
        break
    contador += 1
    soma += num
print(f'A soma dos {contador} valores é {soma}')
