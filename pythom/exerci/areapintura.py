altura = float(input('digite a  altura da parede : '))
largura = float(input('digite a altura da parede  : '))
tinta = (altura * largura) / 2
print('sua parede tem a dimensao de {}x{} e sua area é de {} '.format(altura, largura, altura*largura) )
print('para pintar  essa parede ,  voce presisara de {}L de tinta'.format(tinta))