from random import randint
computador = randint(0,10)
acertou = False
tentativa = 0
print('ESTOU PENSANDO EM UM NUMERO DE ENTRE 0 e 10 ')
print('==========CONSEGUE ADIVINHAR=================')
while not acertou:
    chute= int(input('tente adivinhar: ' ))
    tentativa += 1
    if chute == computador:
        acertou == True
        print('acertou..')
    else:
        if chute < computador:
            print('mais.. ')
        elif chute > computador:
            print('menos..')
print('acetou na {}x '.format(tentativa))