n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outra nota: "))
media = (n1 + n2) / 2

if (media < 5) and (media >= 0):
    print("REPROVADO!")
elif (media >= 5) and media <= 6.9:
    print("RECUPERAÇÃO!")
elif media >= 7:
    print("APROVADO!")
