n1 = int(input('digite um numero :  '))
n2 = int(input(' digite um numero : '))
if  n1 > n2:
    print('o \033[4;32mprimeiro\033[m e \033[4;32m maior\033[m ')
elif n2 >n1:
    print(' o \033[4;32msegundo\033[m é \033[4;32m maior\033[m ')
else:
    print('\033[4;32m ambos sao iguais \033[m')
