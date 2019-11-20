mapeso = 0 #Maior peso
mepeso = 0 #Menor peso
for contador in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(contador)))
    if contador == 1:
        mapeso = peso
        mepeso = peso
    else:
        if mapeso < peso:
            mapeso = peso
        elif mepeso > peso:
            mepeso = peso
print('O maior peso lido foi de {}Kg'.format(mapeso))
print('O menor peso lido foi de {}Kg'.format(mepeso))
