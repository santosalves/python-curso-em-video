def notas(* notas, sit=False):
    """
    :param notas: Valor das notas que será passado como parâmetro
    :param sit: Situação do candidato (Boa, razoável ou ruim, baseado na média)
    :return: Retorna um dicionário com os valores
    """
    media = sum(notas) / len(notas)
    arquivo_notas = {'Quantidade': len(notas), 'Maior nota': max(notas), 'Menor nota': min(notas),
                     'Média': media}
    if sit == True:
        if media >= 7:
            arquivo_notas['Situação'] = 'Boa'
        elif (media >= 5) and (media < 7):
            arquivo_notas['Situação'] = 'Razoável'
        else:
            arquivo_notas['Situação'] = 'Ruim'

    return arquivo_notas


# Programa Principal
resp = notas(5, 5, 1, 8)
print(resp)
