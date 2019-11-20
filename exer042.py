print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Esses segmentos podem formar um triângulo!')

    if n1 == n2 and n1 == n3 and n2 == n3:
        print('Equilatero, todos os lados iguais!')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Isóseles, doi lados iguais.')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('Escaleno, todos os lados diferentes!')
else:
    print('Esses segmentos não podem formar um triângulo!')
