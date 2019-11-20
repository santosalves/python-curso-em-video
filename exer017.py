#A soma dos quadrados dos catetos é igual ao quadrado da hipotenusa

co = float(input('Qual é o comprimento do cateto oposto: '))
ca = float(input('Qual é o comprimento do cateto adjacente: '))

hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa irá medir {:.2f}'.format(hip))
