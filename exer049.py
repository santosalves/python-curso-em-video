n1 = int(input(("Tabuada de qual número?: ")))

for contador in range(1, 11):
    print("{} X {:2} = {:2}".format(n1, contador, n1 * contador))
