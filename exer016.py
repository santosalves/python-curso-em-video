#Importa um função específica dentro da Biblioteca.
#Para importar todos os componentes de uma Biblioteca, basta usar a sintaxe: import (biblioteca).

from math import trunc
n1 = float(input('Digite um número: '))
int = trunc(n1)
print('O valor digitado foi {} e sua porção inteira é {}'.format(n1, int))
