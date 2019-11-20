lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    continuar = str(input('Quer continuar[S/N]?: ')).upper().strip()
    if continuar == 'N':
        break
print(f'A lista completa é  {lista}')
lista2 = lista[:]

for elemento in lista:
    if elemento % 2 == 0:
        lista.remove(elemento)
print(f'A lista com números IMPARES é: {lista}')

#Lista clonada
for elemento in lista2:
    if elemento % 2 == 1:
        lista2.remove(elemento)
print(f'A lista com números PARES é: {lista2}')
