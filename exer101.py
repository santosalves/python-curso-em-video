def voto(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento
    if (idade <= 15) and (idade >= 0):
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif (idade >= 16) and (idade < 18) or idade > 70:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif (idade >= 18) and (idade <= 70):
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


print('-' * 26)
nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))

