from random import randint
v=0
while True:
    j = int(input(' jogue um valor  '))
    compt=  randint(0,11)
    tot = j+compt
    tipo = ' '
    while tipo not in 'pPiI':
        tipo =str(input('\033[1;34mpar ou impar: [P/I] \033[m')).strip().upper()[0]
    print(f'voce jogou \033[1;32m{j}\033[m e o computador \033[1;32m{compt}.\033[m total de \033[1;32m{tot}\033[m')        
    if tipo == 'P':
        if tot %2==0:
            print('\033[1;32mvoce venceu\033[m')
            v+=1
        else:
            print('\033[1;31mvoce perdeu\033[m')
            break
    elif tipo == 'I':
        if tot %2==1:
            print('\033[1;32mvoce ganhou \033[m')
            v+=1
        else:
            print('\033[1;31mvoce perdeu\033[m')
            break
print(f'\033[1;31mGAME OVER\033[m , \033[1;32mVOCE VENCEU {v}x\033[m')