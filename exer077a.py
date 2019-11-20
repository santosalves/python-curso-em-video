palavras = ('PAULO', 'ROBERTO', 'SANTOS', 'ALVES')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for vogal in range(len(palavra)):
        if 'A' in palavra[vogal]:
            print('A',  end=' ')
        elif 'E' in palavra[vogal]:
            print('E',  end=' ')
        elif 'I' in palavra[vogal]:
            print('I',  end=' ')
        elif 'O' in palavra[vogal]:
            print('O',  end=' ')
        elif 'U' in palavra[vogal]:
            print('U',  end=' ')
