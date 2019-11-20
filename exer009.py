n1 = int(input('Digite um número: '))
n2 = -1
n3 = n1 * n2

print('===' * 6)
while n2 <= 9:
    n2 = n2 + 1
    n3 = n1 * n2
    print('{} X {:2} = {}'.format(n1, n2, n3))
print('===' * 6)
