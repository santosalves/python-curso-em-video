print('=' * 25)
print('10 TERMOS DE UMA P.A')
print('=' * 25)

t1 = int(input('Primeiro Termo: '))
razao = int(input('Qual é a Razão: '))
décimo = t1 + (10 - 1) * razao

for contador in range(t1, décimo + razao, razao):
    print('{}'.format(contador), end=" -> ")
print("ACABOU!")
