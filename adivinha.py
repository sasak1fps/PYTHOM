from random import randint                           #faz o computafor escolher 
from time import sleep                               #faz o computador aguardar 
computador = randint(0, 5)
print('=-= ' * 20 )
print('vou pensar em um numero entre 0 e 5 tente adivinha...')
print('=-= ' * 20 )
jogador = int(input('digite um numero escolhido pela maquina :  '))
print('processando.....')
sleep(2)
if jogador == computador:
    print('voce ganhou!!! :)')
else:
    print('voce perdeu , eu pesei no numero {} e não no {}' .format(computador , jogador))
    