preco = float(input("Qual é o valor do Produto: R$: "))
pag = str(input("Qual o método de pagamento(dinheiro/cheque/cartao)?: "))

if pag.lower() == "dinheiro" or pag == "cheque":
    preco = preco - (preco * 10) / 100
    print("O valor é R$: {:.2f}, com 10% de desconto.".format(preco))
elif pag.lower() == "cartao":
    parcelar = input("Deseja parcelar (S/N)?:")
    if parcelar.upper() == "N":
        preco = preco - (preco * 5) / 100
        print("Pagamento à vista.\n O valor é R$: {:.2f}, com 5% de desconto.".format(preco))
    elif parcelar.upper() == "S":
        nparcela = int(input("Deseja fazer em quantas vezes(2,3,4,...)?: "))
        if nparcela == 2:
            print("O preço final é R$: {:.2f}, sem desconto.".format(preco))
            print("A parcela é 2x de R$:{}".format(preco / 2))
        else:
            preco = preco + (preco * 20) / 100
            print("O valor é R$: {:.2f}, com 20% de juros.".format(preco))
            print("A parcela é {}x de R$:{}".format(nparcela, preco / nparcela))
    else:
        print("Opção inválida.")
