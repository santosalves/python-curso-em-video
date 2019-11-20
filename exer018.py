import math
an = float(input('Digite o Ângulo que você deseja: '))
sen = math.sin(math.radians(an))
tan = math.tan(math.radians(an))
cos = math.cos(math.radians(an))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(an, sen))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(an, tan))
print('O ângulo de {:.2f} tem o COSENO de {:.2f}'.format(an, cos))
