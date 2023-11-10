n1=int(input(' primeiro numr : '))
n2=int(input('segundo numero :  '))
opçao= 0
while opçao != 5:
    print('''
[1] somar
[2] multiplicar 
[3] maior 
[4] novos valores
[5] sair   ''')   
    opçao =int(input('qual sua opcao '))
    if opçao==1:
        print('{} + {} = {}'.format(n1,n2,n1+n2))
    elif opçao==2:
        print('{} * {} = {}'.format(n1,n2,n1*n2))
    elif opçao==3:
        if n1 > n2:
            print('{} é maior'.format(n1))
        elif n2 > n1:
            print('{} é maior '.format(n2))
        elif n1 ==n2:
            print('sao iguais')
    elif opçao==4:
        n1=int(input(' primeiro numr : '))
        n2=int(input('segundo numero :  '))
    elif opçao==5:
        print(quit())   
        print('fim!!')
    else:
        print('opcao invalida')
print('fim!!')