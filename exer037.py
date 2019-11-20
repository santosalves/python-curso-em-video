n1 = int(input("Digite um número: "))
print("Escolha uma das bases para conversão:")
print('[1] Binário\n'
      '[2] Hexadecimal\n'
      '[3] Octal\n')
base = int(input("Sua opção: "))

if base == 1:
    print("A conversão de {} para BINÁRIO é {}".format(n1, bin(n1)[2:]))
elif base == 2:
    print("A conversão de {} para HEXADECIMAL é {}".format(n1, hex(n1)[2:]))
elif base == 3:
    print("A conversão de {} para OCTAL é {}".format(n1, oct(n1)[2:]))
else:
    print("Entrada inválida!")
