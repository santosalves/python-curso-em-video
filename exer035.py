print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Esses segmentos podem formar um triângulo!')
else:
    print('Esses segmentos não podem formar um triângulo!')
