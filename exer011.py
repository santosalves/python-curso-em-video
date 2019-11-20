al = float(input('Qual é a altura da parede(m)?: '))
la = float(input('Qual é a largura da parede(m)?: '))
m2 = al * la
lt = m2 / 2
print('Sua parede tem dimensões de {:.2f} X {:.2f} e sua área é {:.2f}m2'.format(al, la, m2))
print("Para pintar esta parede, será necesspario {}L de tinta".format(lt))
