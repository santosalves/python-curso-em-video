from datetime import date

ano = int(input("Em que ano você nasceu?: "))
idade = date.today().year - ano
contador = 0

if idade == 18:
    print("É hora de se alistar!")
elif (idade < 18) and (idade > 0):
    print("Você ainda irá se alistar!")
    while idade < 18:
        idade += 1
        contador += 1
    print("Falta(m) {} ano(s) para você se alistar".format(contador))
elif idade > 18:
    while idade > 18:
        idade -= 1
        contador += 1
    print("Passou {} anos do tempo do alistamento!".format(contador))
