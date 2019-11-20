print('=' * 30, "Financiamento de Imóvel", '=' * 30)
vcasa = float(input("Qual é o valor da casa? R$:"))
salario = float(input("Qual é o seu salário? R$:"))
anos = int(input("Em quantos anos você pretende pagar?: "))
parcelas = float(vcasa / (anos * 12))

if parcelas <= (salario * 30) / 100:
    print("O valor do financiamento é de: R$: {:.2f}".format(parcelas))
    print("O seu financiamento foi aprovado com sucesso!")
else:
    print("O valor do financiamento seria de: R$: {:.2f}".format(parcelas))
    print("O valor é equivalente a mais de 30% do seu salário. Imprestimo negado!")
