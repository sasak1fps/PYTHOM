print('\033[1;33m ======================= JOKENPO ==================\033[m')
from random import randint
from time import sleep

itens = ('pedra' , 'papel' , 'tesoura')
computador = randint( 0 , 2)

print('''\033[1;33m  ESCOLHA UMA OPÇAO            
            [0] PEDRA
            [1] PAPEL
            [2] TESOURA \033[m '''  )

jogador = int(input('qual sua jogada?  '))
print('\033[1;33mJO\033[m')
sleep(1)
print('\033[1;33mKEN\033[m')
sleep(1)
print('\033[1;33mPO!!\033[m')

print('\033[1;36m -=' *12)
print(' o computador escolheu {} '.format(itens[computador ]))
print(' o jogador jogou {}  '.format(itens[jogador]))
print('-= \033[m' * 12 )

if computador == 0:
    if jogador == 0:
        print('\033[1;34m empate\033[m')
    elif jogador ==1:
        print('\033[1;31m voce perdeu   \033[m')
    elif jogador == 2:
        print('\033[1;32mvoce ganhou \033[m')
    else:
        print('\033[1;31m opçao invalida \033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[1;31m voce perdeu \033[m')
    elif jogador ==1:
        print('\033[1;34mempate\033[m')
    elif jogador == 2:
        print('\033[1;32mvoce ganhou \033[m')
    else:
        print('\033[1;31m opçao invalida  \033[m')
elif computador ==2:
    if jogador == 0:
        print('\033[1;32mvoce ganhou\033[m')
    elif jogador ==1:
        print('\033[1;31m voce perdeu \033[m ')
    elif jogador == 2:
        print('\033[1;34mempate\033[m')
    else:
        print('\033[1;31m opçao invalida \033[m ')