ano = int(input("Em que ano você nasceu?: "))
idade = 2017 - ano

if (idade >= 0) and (idade <= 9):
    print("MIRIM")
elif (idade > 9) and (idade <= 14):
    print("INFANTIL")
elif (idade > 14) and (idade <= 19):
    print("JUNIOR")
elif idade == 20:
    print("SENIOR")
elif idade > 20:
    print("MASTER")
