alg = input('Digite Algo: ')
print('O tipo primitivo desse valor é {}'.format(type(alg)))
print('Ele possui espaços? {} '.format(alg.isspace()))
print('Ele é um número? {}'.format(alg.isnumeric()))
print('Ele é decimal? {}'.format(alg.isdecimal()))
print('É uma palavra? {}'.format(alg.isalpha()))